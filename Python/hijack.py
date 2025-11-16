#!/usr/bin/env python3
from scapy.all import *

ip = IP(src="10.9.0.6", dst="10.9.0.7")
#Change the @@@ to the correct ports, seq and ack numbers to spoof a packet
tcp = TCP(sport=@@@, dport=23, flags="A", seq=@@@@, ack=@@@@)
#Change @@@ to the data you want to send
data = "@@@"
pkt = ip/tcp/data
ls(pkt)
send(pkt)


