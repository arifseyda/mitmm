import subprocess
import optparse
import re

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    parse_object.add_option("-m","--mac",dest="mac_adress",help="new mac adress")
    return parse_object.parse_args()

def changeMacAdress(userInterface,userMac):
    subprocess.call(["ifconfig",userInterface,"down"])
    subprocess.call(["ifconfig",userInterface,"hw","ether",userMac])
    subprocess.call(["ifconfig",userInterface,"up"])


def takeMacAdress(userInterface):
    ifconfig = subprocess.check_output(["ifconfig",userInterface])
    newMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if newMac:
        return newMac.group(0)
    else:
        return None

print("My macChanger started")
(userInput,arguments) = get_user_input()
changeMacAdress(userInput.interface,userInput.mac_adress)
finalMac = takeMacAdress(userInput.interface)
if finalMac == userInput.mac_adress:
    print("Success")
else:
    print("Error")