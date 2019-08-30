# How to do mitm attack with python
mitm.py looks like the packet sender and the PacketListener.py listen the packet which produce mitm.py. If you are same network, you listen the http websites. If do you want to listen the https protocols, you use sslstrip and dns2server. So i write SingleTerminal.py. Its title is that open the mitm.py, PacketListener.py sslstrip and dns2proxy with one terminal.

If do you want to use and work this code, you install dns2proxy.

This code don't downgrade https to http every time because some sites have HSTS annd this sites is secure.

Before the starting code, you must write iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000 and iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53 

For working the code: python SingleTerminal.py -i ip adress of the target which you want to attack -g gateway of the target which you want to attack -n  interface of the target which you want to attack -f where are you install the dns2proxy

For example: python SingleTerminal.py -n eth0 -i 192.168.31.131 -g 192.168.31.2 -f /opt/dns2proxy

If do you want learn what is your target ip adress or gateway, you use the NetworkScanner.py
