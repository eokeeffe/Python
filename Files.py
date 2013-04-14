
f = open("HEreIsAfileToOpenOrClose.txt","w")
string1 = "Hello World"
string2 = "Hello Universe"

for i in string1:
	f.write(i)

print f.closed
f.close()
print f.closed
#--------------------------------------------------
f = open("HEreIsAfileToOpenOrClose.txt","a")

for i in string2:
	f.write(i)

print f.closed
f.close()
print f.closed