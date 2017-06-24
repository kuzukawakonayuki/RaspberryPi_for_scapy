from scapy.all import *
import pygame.mixer
import requests

def arp_display(pkt):
    print "0"
    if pkt[ARP].op == 1:
        print "1"
        if pkt[ARP].hwsrc == '88:71:e5:4c:c3:3c':
            print "DashButton Pushed!"
            target_url = 'https://maker.ifttt.com/trigger/Push7_IFTTT/with/key/esNZA0_q9698h1gw9QaAY6PF0mES-A10n9J-pzquQFa'
            r = requests.get(target_url)
            print(r)
            pygame.mixer.init()
            pygame.mixer.music.load("mp3/kusodokata.mp3")
            pygame.mixer.music.play(1)

            print("ctlr+c is stop")
            while True:
                x = 1
    
            pygame.mixer.music.stop()
            sys.exit()

print sniff(prn=arp_display, filter="arp", store=0, count=100)
