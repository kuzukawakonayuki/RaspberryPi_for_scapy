from scapy.all import *
def arp_display(pkt):
    print "0"
    if pkt[ARP].op == 1:
        print "1"
        if pkt[ARP].hwsrc == '88:71:e5:4c:c3:3c':
            print "DashButton Pushed!"
            sys.exit()

print sniff(prn=arp_display, filter="arp", store=0, count=10)
