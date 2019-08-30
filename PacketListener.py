import scapy.all as scapy
from scapy_http import http
import optparse
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!")
    return parse_object.parse_args()

def listen_packets(interface):
    scapy.sniff(iface = interface, store = False, prn = analyzePackets) # prn callback function

def analyzePackets(packet):
    #packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

print("Packet listening started \n")
(userInput,arguments) = get_user_input()
listen_packets(userInput.interface)