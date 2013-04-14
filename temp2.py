import os
import pickle

def createFile(filename,wrtMode,info):
	file = open(filename,wrtMode)
	if(info == 1):
		print 'file:', file
		print 'filename:', file
		print os.path(file)
	return file

def writeSimFile(filehandle,info):
	if(os.path.exists(filehandle.name)):
		filehandle.write(info)
	else:
		report(filename)

def writeComFile(filehandle,LorD):
	if(os.path.exists(filehandle.name)):
		pickle.dump(LorD,filehandle)
	else:
		print filename.name," doesn't exist"

def readSimFile(filehandle,position):
	if(os.path.exists(filehandle.name)):
		filehandle.seek(position)
		for line in filehandle:
			print line
	else:
		print filename.name," doesn't exist"

def readComFile(filehandle):
	if(os.path.exists(filehandle.name)):
		list = pickle.load(filehandle)
		return list
	else:
		print filename.name," doesn't exist"

def closeFile(filehandle):
	filehandle.close()

def removeFile(filehandle,checkhandle):
	if(checkhandle == 0):
		os.remove(filehandle)
	if(checkhandle == 1):
		os.remove(filehandle)
		print 'Deletion completed?:', not(os.path.exists(filehandle))

def report(filename):
	print("file '%s' exists: %s" % (filename, "yes." if os.path.exists(filename.name) else "no."))

name = 'hello.txt'
f = createFile(name,'w+',0)
writeSimFile(f,"hello world")
readSimFile(f,0)
closeFile(f)
removeFile(name,1)