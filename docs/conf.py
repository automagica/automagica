"""
Importeren van benodigde extensies
"""

# Automagica-functionaliteiten
from automagica.activities import Type, PressHotkey, Wait, OpenExcelWorkbook, LaunchProcess, KillProcess

# SAP Interface
import win32com.client

# Nodig voor berekeningen met datum-velden
from datetime import datetime, timedelta

# Nodig om te communiceren met Bizagi
import requests

# Nodig om namen te vergelijken
from fuzzywuzzy import fuzz

# Nodig om ongestructureerde mededelingen te verwerken
import re

# Nodig om matching van kassa-terminals te doen
import fnmatch


"""
Configuratie
"""
#Excel Locaties
locatie_exclusielijst = "C:\Automagica\Master Data\CID\Exclusie Rekeningnummers.xlsx"
locatie_debiteuren_template = "C:\Automagica\Master Data\CID\Template Terugbetaling Debiteuren.xlsx"

# SAP-configuratie
sap_gebruikersnaam = 'M_BIZAGI'
sap_wachtwoord = 'b!zag!'
sap_mandant = '128'
sap_omgeving = 'AE2-H loadbalancing'

# Aantal dagen in het verleden en toekomst met zoekopdracht
aantal_dagen = 30

# Bizagi-configuratie
bizagi_proces_naam = 'RPACases'
bizagi_proces_naam2 = 'RPACases'
bizagi_api_url = 'http://bizagi-demo.eastus.cloudapp.azure.com/AZMMPOC/WebServices/workflowenginesoa.asmx/createCasesAsString'
bizagi_gebruikersnaam = 'admon'
bizagi_domein = 'domain'

# Bankrekeningnummer inningspartner voor interimflow
bankrekeningnummer_inningspartner = 'BE68001478535634'

# Drempelwaarde naamcontrole (bv. 80) gebruiksdoel inningspartner voor interimflow
drempel_naam_controle = 80

# Terminal nummers voor restaurant flow
restaurant_terminals = ["R:*2056225*","R:*2056226*","R:*2056227*"]

# Marge voor onjuiste betalingen in Euro
marge = 1.25

# Parameters voor de afrondingen flow
bksl_positief = 50
bksl_negatief = 40
reknr_positief = 705900
reknr_negatief = 709009
mededeling_te_weinig_betaald = "Te weinig betaald"
mededeling_te_veel_betaald = "Te veel betaald"
kostenplaats_luik_A = 8300
kostenplaats_luik_B = 1440

# Parameters voor de terugbetaling flow
terugbetaling_excel_robot_init = "ROBOT"

"""
Functies
"""

def check_zero_sums(values, sum_goal=0):
    """ This function checks whether any possible sum returns zero """
    from itertools import combinations
    zero_sums = []
    values = [round(value,2) for value in values]
    for i in range(0, len(values)+1):
        for subset in combinations(values, i):
            if round(sum(subset),2) == round(sum_goal,2):
                zero_sums.append([values.index(item) for item in subset])
    return zero_sums

def create_bizagi_case(case):
    """ This function creates a case in Bizagi """
    bizagi_case_info = '''<BizAgiWSParam>
                            <domain>'''+bizagi_domein+'''</domain>
                            <userName>'''+bizagi_gebruikersnaam+'''</userName>
                            <Cases>
                                <Case>
                                    <Process>'''+bizagi_proces_naam+'''</Process>
                                    <Entities>
                                        <'''+bizagi_proces_naam+'''>
                                            '''+''.join(['<'+key+'>'+str(value)+'</'+key+'>\n' for key, value in case.items()])+'''
                                            <procesnaam>'''+bizagi_proces_naam2+'''</procesnaam>
                                        </'''+bizagi_proces_naam+'''>
                                    </Entities>
                                </Case>
                            </Cases>
                          </BizAgiWSParam>''' 
    print(bizagi_case_info)
    return requests.get(bizagi_api_url, params={'casesInfo': bizagi_case_info}, timeout=2)

def check_zero_sums_afronding(values, sum_goal=0, marge=marge):
    """ This function checks whether any possible sum returns zero """
    import itertools
    zero_sums = []
    sum_values = []
    for i in range(0, len(values)+1):
        for subset in itertools.combinations(values, i):
            if round((sum_goal - marge),2) <= round(sum(subset),2) <= round((sum_goal + marge),2):
                zero_sums.append([values.index(item) for item in subset])
                sum_values.append(sum(subset))
    return zero_sums, sum_values

"""
Login SAP
"""

# Start SAP en sla de referentie op voor later
sap_process = LaunchProcess('C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe')

# Verbinden met SAP GUI
Wait(seconds=3)
sapgui = win32com.client.GetObject("SAPGUI").GetScriptingEngine

# Maak verbinding met de SAP omgeving
connection = sapgui.OpenConnection(sap_omgeving, True)

# Identificeer de sessie
sap = sapgui.FindById("ses[0]")

# Log in op SAP
sap.findById("wnd[0]/usr/txtRSYST-MANDT").text = sap_mandant
sap.findById("wnd[0]/usr/txtRSYST-BNAME").text = sap_gebruikersnaam
sap.findById("wnd[0]/usr/pwdRSYST-BCODE").text = sap_wachtwoord
sap.findById("wnd[0]").sendVKey(0)


# Ga verder met login indien al ingelogd
try:
    sap.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").select()
    sap.findById("wnd[1]/usr/radMULTI_LOGON_OPT2").setFocus()
    sap.findById("wnd[1]/tbar[0]/btn[0]").press()
except:
    pass

# Initialiseer de sap sessie counter
global_sap_session = 1

"""
Start FEBAN-transactie
"""

# Start FEBAN-transactie
sap.StartTransaction("FEBAN")

# Vul bedrijfsnummer in
sap.findById("wnd[1]/usr/ctxtSL_BUKRS-LOW").text = "ZH00"

# Bereken datum-velden
# vandaag = datetime.today()
vandaag = datetime.strptime('07.02.2018','%d.%m.%Y')
start_datum = (vandaag - timedelta(days=aantal_dagen)).strftime('%d.%m.%Y')
eind_datum = (vandaag + timedelta(days=aantal_dagen)).strftime('%d.%m.%Y')

# Vul overzichtsdatum van in
sap.findById("wnd[1]/usr/ctxtSL_AZDAT-LOW").text = start_datum

# Vul overzichtsdatum tot in
sap.findById("wnd[1]/usr/ctxtSL_AZDAT-HIGH").text = eind_datum

# Vul boekingsgebied 1 OK
sap.findById("wnd[1]/usr/ctxtSL_VB1OK-LOW").text = "X"

# Vul boekingsgebied 2 OK
sap.findById("wnd[1]/usr/ctxtSL_VB2OK-LOW").setFocus()
sap.findById("wnd[1]").sendVKey(2)
sap.findById("wnd[2]").sendVKey(2)

# Voer zoekopdracht uit
sap.findById("wnd[1]").sendVKey(8)

# Verander weergave
sap.findById("wnd[0]/tbar[1]/btn[14]").press()


"""
Filter exclusielijst
"""

# Selecteer bankrekeningnummer-kolom
sap.findById("wnd[0]/shellcont/shell").selectColumn("PIBAN")

# Klik op filteren
sap.findById("wnd[0]/shellcont/shell").pressToolbarButton("&MB_FILTER")

# Klik op meerdere waarden-knop
sap.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/btn%_%%DYN001_%_APP_%-VALU_PUSH").press()

# Afzonderlijke waarden uitsluiten
sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpNOSV").select()

# Open de exclusielijst
excel_workbook =  OpenExcelWorkbook(locatie_exclusielijst)
exclusielijst = excel_workbook['Blad1']
bankrekening_nummers = [row[1].value for row in exclusielijst.rows]

# Voer bankrekeningnummers in
for i, bankrekening_nummer in enumerate(bankrekening_nummers):
    # Regel toevoegen
    sap.findById("wnd[2]/tbar[0]/btn[13]").press()
    # Vul veld in
    sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpNOSV/ssubSCREEN_HEADER:SAPLALDB:3030/tblSAPLALDBSINGLE_E/ctxtRSCSEL_255-SLOW_E[1,0]").text = bankrekening_nummer

# Opslaan
sap.findById("wnd[2]/tbar[0]/btn[8]").press()

# Uitvoeren
sap.findById("wnd[1]/tbar[0]/btn[0]").press()

"""
Filter rappels en gestructureerde mededeling deelbetaling gebruiksdoelen met 77* en 67*
"""
# Selecteer kolom gebruiksdoel
sap.findById("wnd[0]/shellcont/shell").selectColumn("VWEZW")

# Klik op filter-knop
sap.findById("wnd[0]/shellcont/shell").pressToolbarButton("&MB_FILTER")

# Open meerdere waarden venster
sap.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/btn%_%%DYN001_%_APP_%-VALU_PUSH").press()

# Uitsluiting meerdere waarden tabblad
sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpNOSV").select()

# Waarden
sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpNOSV/ssubSCREEN_HEADER:SAPLALDB:3030/tblSAPLALDBSINGLE_E/ctxtRSCSEL_255-SLOW_E[1,0]").text = "77*"
sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpNOSV/ssubSCREEN_HEADER:SAPLALDB:3030/tblSAPLALDBSINGLE_E/ctxtRSCSEL_255-SLOW_E[1,1]").text = "67*"

# Opslaan
sap.findById("wnd[2]/tbar[0]/btn[8]").press()

# Uitvoeren
sap.findById("wnd[1]/tbar[0]/btn[0]").press()

"""
Filter positieve bedragen
"""
# Selecteer bedragkolom
sap.findById("wnd[0]/shellcont/shell").selectColumn("KWBTR")

# Klik op filterknop
sap.findById("wnd[0]/shellcont/shell").pressToolbarButton("&MB_FILTER")

# Vul 0 in
sap.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").text = "0"
sap.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/ctxt%%DYN002-LOW").setFocus()

# Kies groter dan
sap.findById("wnd[1]").sendVKey(2)
sap.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").currentCellRow = 3
sap.findById("wnd[2]/usr/cntlOPTION_CONTAINER/shellcont/shell").selectedRows = "3"
sap.findById("wnd[2]").sendVKey(2)

# Uitvoeren
sap.findById("wnd[1]/tbar[0]/btn[0]").press()

"""
Filter op test-case indien we aan het testen zijn
"""
TESTING = True

if TESTING:
    test_cases_excel = OpenExcelWorkbook("C:\Automagica\Testing\CID\Test Cases - Betalingsbeheer RPA_dubbel.xlsx")
    test_cases = test_cases_excel['Cases']
    sap.findById("wnd[0]/shellcont/shell").selectColumn("BELNR")
    sap.findById("wnd[0]/shellcont/shell").pressToolbarButton("&MB_FILTER")
    sap.findById("wnd[1]/usr/ssub%_SUBSCREEN_FREESEL:SAPLSSEL:1105/btn%_%%DYN005_%_APP_%-VALU_PUSH").press()
    for index, test_case in enumerate(test_cases):
        if index != 0:
            if test_case[6].value == 'x':
                sap.findById("wnd[2]/tbar[0]/btn[13]").press()
                sap.findById("wnd[2]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = int(test_case[2].value)
    sap.findById("wnd[2]/tbar[0]/btn[8]").press()
    sap.findById("wnd[1]/tbar[0]/btn[0]").press()


"""
Maak werklijst robot
"""
werklijst = []

# Lees tabel uit SAP
for i in range(0, 1000):
    try:
        item = {}
        # Selecteer i-de rij
        sap.findById("wnd[0]/shellcont/shell").setCurrentCell(i, "")

        # Lees waarden uit de tabel voor de i-de rij
        item['gebruiksdoel'] = sap.findById("wnd[0]/shellcont/shell").GetCellValue(i,'VWEZW')
        item['documentnummer'] = sap.findById("wnd[0]/shellcont/shell").GetCellValue(i,'BELNR')
        item['rekeningnummerzakenpartner'] = sap.findById("wnd[0]/shellcont/shell").GetCellValue(i,'PIBAN')
  
        # Maak ruimte voor foutmelding
        item['foutmelding'] = None
        totaalbedrag = sap.findById("wnd[0]/shellcont/shell").GetCellValue(i,'KWBTR')
  
        # Converteer SAP-notatie van bedragen naar float voor berekeningen
        item['totaalbedrag'] = float(totaalbedrag.replace('.','').replace(',','.'))

        item['totaalbedrag_sap_format'] = totaalbedrag
  
        # Voeg item toe aan werklijst
        werklijst.append(item)    
  
    except:
        pass

"""
Voer werklijst uit
"""

for item in werklijst:
    # Controleer of we op het hoofdscherm zitten, zoniet zorg dat we er geraken
    while 'rekeningoverzichten bewerken' not in sap.findById('wnd[0]/titl').text.lower():
        sap.findById("wnd[0]").sendVKey(12)
        try:
            sap.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
        except:
            pass
        
# Dubbele betaling of iets anders
sap.createSession()
print("We zitten dubbele betalingen")
Wait(5)
sap2 = sapgui.FindById("ses["+str(global_sap_session)+"]")
sap2.findById("wnd[0]/tbar[0]/okcd").text = "FB03"
sap2.findById("wnd[0]").sendVKey(0)

# Variabelen meegeven
gebruiksdoel = item['gebruiksdoel']
bedrag = round(item['totaalbedrag'],2)

#Aanpassen naar klassieke rooster weergave voor de zekerheid
sap2.findById("wnd[0]/tbar[1]/btn[16]").press()
sap2.findById("wnd[0]/usr/tabsTS/tabp1103/ssubS1103:SAPMF05O:1103/radRFOPT2-XDLST").select()
sap2.findById("wnd[0]/tbar[0]/btn[3]").press()

#Invullen van gebruiksdoel en datum
sap2.findById("wnd[0]/usr/txtRF05L-BELNR").text = gebruiksdoel
sap2.findById("wnd[0]/usr/ctxtRF05L-BUKRS").text = "ZH00"
sap2.findById("wnd[0]/usr/txtRF05L-GJAHR").text = "20" + str(gebruiksdoel[:2])
sap2.findById("wnd[0]").sendVKey(0)


# Bouw lijst met mogelijke opties
sap2.findById("wnd[0]/usr/lbl[1,13]").setFocus()
sap2.findById("wnd[0]").sendVKey(2)

for i in range(1,10):
    try:
        tijdelijk_bedrag = round(float(sap2.findById("wnd[0]/usr/txtBSEG-WRBTR").text.replace(" ","").replace(",",".")),2) 
        tijdelijk_debiteur = sap2.findById("wnd[0]/usr/txtBSEG-WRBTR").text

        if tijdelijk_bedrag == bedrag and tijdelijk_debiteur[:1] is not "V":

            try:
                eerste_betaling_docnummer = sap2.findByID("wnd[0]/usr/txtBSEG-AUGBL").text
                debiteur = sap2.findByID("wnd[0]/usr/ctxtKNA1-KUNNR").text
                aanmaangebied_luik = sap2.findByID("wnd[0]/usr/ctxtBSEG-MABER").text
                eerste_betaling_datum = sap2.findByID("wnd[0]/usr/ctxtBSEG-AUGDT").text
                documentnummer_terugbetaling = sap2.findById("wnd[0]/usr/txtBSEG-BELNR").text
                naam_begunstigde = sap2.findById("wnd[0]/usr/txtKNA1-NAME1").text
                break
            except:
                pass
        sap2.findById("wnd[0]/tbar[1]/btn[19]").press()

    except:
        item['foutmelding'] = "Gezocht of het gaat om dubbele betaling, maar kan geen vereffening vinden voor dubbele betaling of niet alle benodigde gegevens (Vereffeningsdatum en -document etc.. ) gevonden voor terugbetaling."
    # Zoek naar een vorige vereffening

# Terug naar het FB03 overzicht
sap2.findById("wnd[0]/tbar[0]/btn[15]").press()
sap2.findById("wnd[0]/tbar[0]/btn[15]").press()

# Opzoeken eerste betaling
sap2.findById("wnd[0]/usr/txtRF05L-BELNR").text = eerste_betaling_docnummer
sap2.findById("wnd[0]/usr/ctxtRF05L-BUKRS").text = "ZH00"
sap2.findById("wnd[0]/usr/txtRF05L-GJAHR").text = eerste_betaling_datum[-4:]
sap2.findById("wnd[0]").sendVKey(0)

# Opzoek naar terugbetalingsrekening, eerst zoeken naar item waarvoor Bs = 15
sap2.findById("wnd[0]/usr/lbl[1,13]").setFocus()
sap2.findById("wnd[0]").sendVKey(2)

# Voor elk item zoeken of hier een bankrekenignummer te vinden is
mededeling= ""
for i in range(1,4):
    try:
        tijdelijk_bedrag = round(float(sap2.findById("wnd[0]/usr/txtBSEG-WRBTR").text.replace(" ","").replace(",",".")),2) 
        tijdelijk_debiteur = sap2.findById("wnd[0]/usr/txtBSEG-WRBTR").text

        if int(sap2.findByID("/app/con[0]/ses[1]/wnd[0]/usr/boxRF05L-BSTXT").text[-2:]) == 15:
            
                # Ga naar de 'relationship browser' in het hoofdmenu door omgeving->documentomgeving->rel. browser.
                sap2.findById("wnd[0]/mbar/menu[4]/menu[6]/menu[4]").select()
                # Selecteer tweede item, afzonderlijke posten rekening.
                sap2.findById("wnd[0]/usr/cntlBROWSER/shellcont/shell/shellcont[1]/shell[1]").unselectNode("          1")
                sap2.findById("wnd[0]/usr/cntlBROWSER/shellcont/shell/shellcont[1]/shell[1]").selectNode("          2")
                sap2.findById("wnd[0]/tbar[1]/btn[2]").press()
                # Scannen van tekst in alle vakjes en toevoegen aan mededeling om zo de volledige ongestructureerde mededeling op te halen:
                mededeling = ""
                for i in range(0,150):
                    for j in range(10,30):
                        try:
                            mededeling += sap2.findById("wnd[0]/usr/lbl["+str(i)+","+str(j)+"]").text
                        except:
                            pass                          
    except:
        pass
    sap2.findById("wnd[0]/tbar[1]/btn[19]").press()

eerste_betaling_bankrekeningnummer = ""
bankerekeningnummer = ""

if item['rekeningnummerzakenpartner'] in mededeling:
    eerste_betaling_bankrekeningnummer = item['rekeningnummerzakenpartner']
    bankrekeningnummer = item['rekeningnummerzakenpartner']
# Bekijken of er een ongestructureerde mededeling is gevonden
elif len(mededeling) > 5:
    item['foutmelding'] = "Ongestructureerd gebruiksdoel gevonden en bekeken, maar geen overeenkomend bankrekeningnummer gevonden"
else:
    item['foutmelding'] = "Bankrekeningnummer voor terugbetaling van dubbele betaling niet gevonden"

# Ophalen bankrekeningnummer
#eerste_betaling_bankrekeningnummer = item['rekeningnummerzakenpartner'] # TIJDELIJK (WANT GEEN CASE BESCHIKBAAR)
#bankrekeningnummer = item['rekeningnummerzakenpartner']

# Sap venster sluiten en global sessie variabele incrementeren
sap2.findById("wnd[0]").close()
global_sap_session = global_sap_session + 1
'''
# Controleren of bankrekeningnummer van eerste betaling overeenkomt met bankrekeningnummer van latere (dubbele) betaling
if not eerste_betaling_bankrekeningnummer == bankrekeningnummer:
    item['foutmelding'] = "Bankrekeningnummer eerste en tweede betaling komen niet overeen. Bankrekeningnummer eerste betaling: " + str(eerste_betaling_bankrekeningnummer) + "Bankrekeningnummer tweede betaling: " + str(bankrekeningnummer)
    continue
else:
    pass
'''
### Verwerken van de dubbele betaling in SAP

# Nieuwe sessie openen
sap.createSession()
# Ga naar FB5LN
Wait(5)
sap2 = sapgui.FindById("ses["+str(global_sap_session)+"]")
sap2.findById("wnd[0]/tbar[0]/okcd").text = "FBL5N"
sap2.findById("wnd[0]").sendVKey(0)

# Vul debiteur in en selecteer juiste luik: alle posten aanvinken
sap2.findById("wnd[0]/usr/ctxtDD_KUNNR-LOW").text = debiteur
sap2.findById("wnd[0]/usr/radX_AISEL").select()

# Ga naar volgende scherm (klokje met vinkje linksboven klikken)
sap2.findByID("wnd[0]/tbar[1]/btn[8]").press()

# Ga naar volgende scherm
sap2.findById("wnd[0]/tbar[1]/btn[34]").press()

# Dubbele betalingen betalingsinformatie om IBAN uit BBAN te verkrijgen
landcode = eerste_betaling_bankrekeningnummer[:2]
bban = eerste_betaling_bankrekeningnummer[4:][:3] + '-' + eerste_betaling_bankrekeningnummer[7:][:-2] + '-' + eerste_betaling_bankrekeningnummer[-2:]

# Ga naar details en vul gegevens in
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03").select()
sap2.findById("wnd[0]/tbar[1]/btn[5]").press()
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0202/subAREA1:SAPMF02D:7131/tblSAPMF02DTCTRL_ZAHLUNGSVERKEHR/ctxtKNBK-BANKS[0,0]").setFocus()
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0202/subAREA1:SAPMF02D:7131/tblSAPMF02DTCTRL_ZAHLUNGSVERKEHR/ctxtKNBK-BANKS[0,0]").text = landcode
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0202/subAREA1:SAPMF02D:7131/tblSAPMF02DTCTRL_ZAHLUNGSVERKEHR/ctxtKNBK-BANKL[1,0]").text = eerste_betaling_bankrekeningnummer[4:][:3]
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0202/subAREA1:SAPMF02D:7131/tblSAPMF02DTCTRL_ZAHLUNGSVERKEHR/txtKNBK-BANKN[2,0]").text = bban
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB03/ssubSUBSC:SAPLATAB:0202/subAREA1:SAPMF02D:7131/tblSAPMF02DTCTRL_ZAHLUNGSVERKEHR/btnIBAN[5,0]").press()
sap2.findById("wnd[1]/tbar[0]/btn[0]").press()
# Klik op het vinkje om de pop-up te sluiten
sap2.findById("wnd[1]/tbar[0]/btn[0]").press()

# Klik op gegevens bedrijfsnummer en ga naar betalingsverkeer om S in te vullen voor betalingswijzen
sap2.findById("wnd[0]/tbar[1]/btn[26]").press()
sap2.findById("wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02").select()
sap2.findById("/app/con[0]/ses[2]/wnd[0]/usr/subSUBTAB:SAPLATAB:0100/tabsTABSTRIP100/tabpTAB02/ssubSUBSC:SAPLATAB:0202/subAREA2:SAPMF02D:7216/ctxtKNB1-ZWELS").text = "S"
# Saven
sap2.findById("/app/con[0]/ses[2]/wnd[0]/tbar[0]/btn[11]").press()

# Sluiten van window en sessie counter incrementeren
sap2.findById("wnd[0]").close()
global_sap_session = global_sap_session + 1

## Invullen Excel Tempplate

# Opbouwen parameterset
data = [terugbetaling_excel_robot_init, debiteur, documentnummer_terugbetaling, naam_begunstigde, item['totaalbedrag'], aanmaangebied_luik]

# Open debiteuren templateme
workbook = OpenExcelWorkbook(locatie_debiteuren_template)

# Open tabblad voor terugbetalingen aan patienten
sheet = workbook['Terugbetaling aan patienten']

# Vind eerste lege rij
first_empty_row = None
for row in sheet:
    if not row[0].value:
        first_empty_row = row
        break

# Vul rij in
for col, field in enumerate(data):
    first_empty_row[col].value = field

# Sla Excel op
workbook.save(locatie_debiteuren_template)

## Wegboeken dubbele betaling # To Do
            continue

            else:
                item['foutmelding'] = 'Dit item valt niet binnen de scope van de robot.'
                continue
    except:
        item['foutmelding'] = 'Dit item kon niet verwerkt worden door de robot door onbekende redenen.'
        continue


KillProcess(sap_process)