# Creator: UrielYochpaz
# This script parse a pcap file; Gets the load data in ICMP Packets [The Reciver] 

from scapy.all import *

pacs = scapy.all.rdpcap(r'/root/Downloads/pic_in_icmp.pcap')
data= ''
for p in pacs:
	if 'ICMP' in p:
		data = data+p.getlayer('ICMP').load

with open(r'\root\Desktop\pic.jpg', 'wb') as pic:
	pic.write(data)
