#MY Mexican Army code
list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

modulo = [06,32,73,94]

def MexicanAmryCode(list,K,mod):
	for i in list:
		print i + K % mod


MexicanAmryCode(list,modulo[0],modulo[0])
print "\r\n"
MexicanAmryCode(list,modulo[1],modulo[1])
print "\r\n"
MexicanAmryCode(list,modulo[2],modulo[2])
print "\r\n"
MexicanAmryCode(list,modulo[3],modulo[3])
print "\r\n"