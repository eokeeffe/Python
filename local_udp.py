import socket

UDP_IP = "localhost"
UDP_PORT = 57661
MESSAGE = "off"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
print "Message sent"