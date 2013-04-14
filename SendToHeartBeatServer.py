import socket
import time

UDP_IP = "receiver ip_address here"
UDP_PORT = 12345
MESSAGE = "here is lots of data"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP	
sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
print "Messages sent,please go to the gmail account to get the warning"