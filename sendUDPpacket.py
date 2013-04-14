import socket
import time
from random import randrange, uniform

UDP_IP = "localhost" #raw_input("Enter IP Address:")
UDP_PORT = 9876 #int(raw_input("Enter the port to send to:"))

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP	
i = 0
while i < 10:
	irand = randrange(1, 3)
	erand = randrange(0, 123456)
	MESSAGE = str(irand)+":"+str(erand)
	sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
	i+=1

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

print "Messages sent,Check Database to see if it updated correctly"