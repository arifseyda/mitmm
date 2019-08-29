import scapy.all as scapy
import optparse

def get_ipAdress():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ipAdress", dest="ipAdress", help="Enter ip adress")
    (userInput, arguments) =  parse_object.parse_args()
    if not userInput.ipAdress:
        print("Enter ip adress")
    return userInput
def networkScan(ip):
    arpPacket = scapy.ARP(pdst=ip)
    brodcastPacet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combinedPacket = brodcastPacet / arpPacket
    (answered,unanswered) = scapy.srp(combinedPacket,timeout=1)
    answered.summary()

userIp = get_ipAdress()
networkScan(userIp.ipAdress)