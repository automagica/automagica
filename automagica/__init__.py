import os
import sys
from sty import bg, rs, fg
from socketIO_client import SocketIO

from .auth import Auth
from .bot import Bot
from .activities import *


def start():
    os.system('cls')

    if len(sys.argv) > 1:
        bot_id = sys.argv[1]
    else:
        bot_id = input('Please provide your Automagica Bot ID: \n')

    if len(sys.argv) > 2:
        host = sys.argv[2]
    else:
        host = 'https://automagica.be'

    if len(sys.argv) > 3:
        port = sys.argv[3]
    else:
        port = None

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
    print(fg.li_cyan + 'Automagica Bot (' + bot_id +
          ') launched and waiting! Listening to ' + host + rs.bg)
    socketIO = SocketIO(host, port)
    bot = Bot
    bot.bot_id = bot_id
    bot_namespace = socketIO.define(bot, '/bot')

    bot_namespace.emit('auth', {'bot_id' : bot_id})

    socketIO.wait()


if __name__ == '__main__':
    start()
