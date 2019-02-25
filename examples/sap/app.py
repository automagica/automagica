import win32com.client

"""
Performs transaction FEBAN within SAP GUI
Requires scripting engine within SAP GUI to be enabled.

This works only on Windows platform, because SAP GUI only supports Windows.
"""

sapgui = win32com.client.GetObject("SAPGUI").GetScriptingEngine

sap = sapgui.FindById("ses[0]")

sap.StartTransaction("FEBAN")

sap.FindById("/app/con[0]/ses[0]/wnd[1]/usr/ctxtSL_BUKRS-LOW").text = "1234"

sap.FindById("/app/con[0]/ses[0]/wnd[1]/usr/ctxtSL_BUKRS-HIGH").text = "5678"

sap.FindById("/app/con[0]/ses[0]/wnd[1]/usr/ctxtSL_HBKID-LOW").text = "9012"


