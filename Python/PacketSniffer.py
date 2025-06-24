from scapy.all import *

def process_packet(packet):
    #Print out each captured packet.
    print(packet.summary())

if __name__ == "__main__":
    # For Linux, set interface="eth0" or desired interface name.
    # For Windows, set iface=None or desired interface name.
    interface = None
    try:
        #Calls the function to print the packets on the set interface.
        sniff(prn = process_packet, iface = interface, store = 0)
    except KeyboardInterrupt:
        #stops the program with ctrl+c
        print("\nSniffing stopped.")