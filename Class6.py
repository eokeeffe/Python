"""
	Traceback logs and how to use command line
	debugger commands
	
	The way to do this in command line is
	
	python -m pdb x.py where x.py is the python modules name
	
	- s is for stepping through the pdb
	- n is for the running the current line and then the next
	- c for continuing the program until next break point
	- r run the program until the return of the current function
	- l display source code around current line
	- a display current function arguements
	- p print expression
	- pp pretty-print expression
	- q quit the debugger and the program
	- b # set a break point at the line number
"""

print "This function creates a list"
def makelist():
	a =[]
	for i in range(1,20):
		a.append(i)
		print "Appending",i,":",a
	return a

makelist()
