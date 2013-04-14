import os
#merge all files in a directory into a single file
path = 'Directory to read'
listing = os.listdir(path)
dictfile = open("somefile","w")
for infile in listing:
	f = open(path+"\\"+infile,"r")
	for i in f.read():
		dictfile.write(i)
	f.close()
	print "file: " + infile + " finished"
dictfile.close()