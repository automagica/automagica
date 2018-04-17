from time import sleep
from socketIO_client import BaseNamespace
from .activities import *
from sty import bg, rs, fg

class Bot(BaseNamespace):
    bot_id = None

    def on_run(self, data):
        try:
            print('Received job #' + str(data['job_id']))
            exec(data['code'], globals())
            print('Finished job #' + str(data['job_id']) +' successfully.')
            self.emit('finish', {'type': 'success', 'bot_id': self.bot_id, 'job_id': data['job_id']})
        except Exception as e:
            print('Failed job #' + str(data['job_id']))
            print('Exception: ' + str(e))
            self.emit('finish', {'type': 'failure', 'bot_id': self.bot_id, 'job_id': data['job_id'], 'exception': str(e)})

    def on_connect(self):
        os.system('cls')
        print(fg.li_cyan + """
          sdNMMMd+                                                                                                     
        .oNMMMNNMMN:                                                                         +mmh.                     
       oNMMd+.  yMMy             :`                                                          dMMM:                     
     `dMMm:     yMMy            oMMm                                                          -:.                      
    `mMMh`     .MMM:/oo/ .ooo.ooMMMh+  -+sys/`     +oo+/o+. -+o+.       `-/+o:      .:/++o. /oo/    :oyyy+`     `-/+o+ 
.:::yMMN:::::::hMMd-MMM: dMMyyMMMMMM/.hMMMMMMNo::.+MMMMMMMMNMMMMM-   :yNMMMMMy  `odNMMMMMM-:MMM-  +mMMMMMMh  -smMMMMMm 
oMMMMMMMMMMMMMMMMM.mMMs oMMN``sMMN.``NMMhsMMMMMMN-NMMMdoMMMMdoMMM: .dMMNyhh+-` /NMMms/shs/`mMMs `dMMN+`+yy+`yMMMhhdo:` 
+//sMMM+/////oMMM++MMN./MMM/ -MMM:  -MMM/`/NMMm/-hMMN/ hMMN/ hMMh  mMMy`/MMM/ .MMM+`:hMMMosMMm` oMMm`      hMMd.-NMMs  
   `MMM-     hMMd :MMMMMMMMMNhMMMMMM+sMMMMMMMh` /MMN. +MMN.  NMMMMsmMMNNMMMMMMNNMMMMMMMMd mMMMMMdMMMMMMMMMMmMMNNMMMMMMM
    hMMy    .yyy.  .+sso:/sy+ /syyys  .+sys+.   syy:  syy/   .oyys``+yhhs+syyy/`/syshMMM- `oyyyo :oyyyyyyys /shhs+oyyyo
    -MMm.                                                                          .NMMo                               
     .                                                                           `+NMMy                                
                                                                              +sdMMMm/                                 
                                                                              yMNds-                                   
""" + rs.bg)
        print(fg.li_cyan + 'Automagica Bot (' + self.bot_id +
          ') launched and waiting!')
        print('Connected!')
        self.emit('auth', {'bot_id' : self.bot_id})

    def on_disconnect(self):
        print('Disconnected!')

    def on_reconnect(self):
        os.system('cls')
        print(fg.li_cyan + """
          sdNMMMd+                                                                                                     
        .oNMMMNNMMN:                                                                         +mmh.                     
       oNMMd+.  yMMy             :`                                                          dMMM:                     
     `dMMm:     yMMy            oMMm                                                          -:.                      
    `mMMh`     .MMM:/oo/ .ooo.ooMMMh+  -+sys/`     +oo+/o+. -+o+.       `-/+o:      .:/++o. /oo/    :oyyy+`     `-/+o+ 
.:::yMMN:::::::hMMd-MMM: dMMyyMMMMMM/.hMMMMMMNo::.+MMMMMMMMNMMMMM-   :yNMMMMMy  `odNMMMMMM-:MMM-  +mMMMMMMh  -smMMMMMm 
oMMMMMMMMMMMMMMMMM.mMMs oMMN``sMMN.``NMMhsMMMMMMN-NMMMdoMMMMdoMMM: .dMMNyhh+-` /NMMms/shs/`mMMs `dMMN+`+yy+`yMMMhhdo:` 
+//sMMM+/////oMMM++MMN./MMM/ -MMM:  -MMM/`/NMMm/-hMMN/ hMMN/ hMMh  mMMy`/MMM/ .MMM+`:hMMMosMMm` oMMm`      hMMd.-NMMs  
   `MMM-     hMMd :MMMMMMMMMNhMMMMMM+sMMMMMMMh` /MMN. +MMN.  NMMMMsmMMNNMMMMMMNNMMMMMMMMd mMMMMMdMMMMMMMMMMmMMNNMMMMMMM
    hMMy    .yyy.  .+sso:/sy+ /syyys  .+sys+.   syy:  syy/   .oyys``+yhhs+syyy/`/syshMMM- `oyyyo :oyyyyyyys /shhs+oyyyo
    -MMm.                                                                          .NMMo                               
     .                                                                           `+NMMy                                
                                                                              +sdMMMm/                                 
                                                                              yMNds-                                   
""" + rs.bg)
        print(fg.li_cyan + 'Automagica Bot (' + self.bot_id +
          ') launched and waiting!')
        print('Connected!')
        self.emit('auth', {'bot_id' : self.bot_id})