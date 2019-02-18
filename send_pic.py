# Creator: UrielYochpaz
# This script transfer data via ICMP packets [The sender]

from scapy.all import *

# Constants
IP = '10.10.10.1' # Destination ip
SIZE = 1024 # Bites to transfer every packet
PATH = r"/root/Desktop/Picture.jpg" # File to transfer 

with open(PATH, 'rb') as pic:
    data = pic.read()

print "[+] Starting Sending Data..."
while data != '':
    packet=IP(dst=IP)/ICMP()/data[:SIZE]
    scapy.all.send(packet)
    data = data.replace(data[:SIZE], '')

print "[+] Transfer Data Via ICMP Done!\n"


