# How to do mitm attack with python
mitm.py looks like the packet sender and the PacketListener.py listen the packet which produce mitm.py. If you are same network, you listen the http websites. İf do you want to listen the https protocols, you use sslstrip and dns2server. So ı do SingleTerminal.py. Its title is that opening the mitm.py, PacketListener.py sslstrip and dns2proxy with one terminal.

If dou you want to use and work this code, you install dns2proxy which downloads in home file. İf do you want to download other folder, you change SingleTerminal.py 8. line. 

You change the ip adress interface at code because of the working code your network.

This code don't downgrade https to http every time becouse some sites have HSTS annd this sites is secure.
