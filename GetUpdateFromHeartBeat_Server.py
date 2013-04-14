import socket

UDP_IP = "some sefver"
UDP_PORT = 57661
MESSAGE = "UPDATE_ME"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
print "Message sent,please go to the gmail account to get the log"