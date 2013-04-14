"""
	Now you should be able to see the documentation for the
	module in the file and also in the console
	
	So here are a couple of functions with the pydoc for each
	and also how to make commments in the code itself
"""

#def is used to define functions in python

def tinyFunction():
	"""
		Now you should be able to see the documentation for the
		function in here
	"""
	x = "And now you know how to import individual"
	y = " modules in python"
	print x,y
	
def AnotherFunction(x):
	"""
		Here is where you put the documentation
		this function will take a number and return a power
	"""
	return (x*x)
	
def ComplexPrinting():
	"""
		This is how to use and print 
		Complex numbers
	"""
	a = 3+2j
	b = 2+3j
	
	print "Complex a=",a,"Complex b=",b
	print "real a: ",a.real,"|imaginary a: ",a.imag
	print "real b: ",b.real,"|imaginary b: ",b.imag
	print "a+b=",a+b
	
def Tuples():
	"""
		How to use tuples and print them
	"""
	x = ("a",2,"33")
	print x
	
	#so like java , python has the iterator class
	
	for i in x:
		print i
	
def Lists():
	"""
		How to use lists and print them
	"""
	x = ['here','is','my','list',47]
	print x
	
	#so like java , python has the iterator class
	
	for i in x:
		print i
		
def Dictionaries():
	"""
		How to use Dictionaries
	"""
	swallow_velocity = {"european":"47","African":"69"}
	
	myList = ['spam','lovely','spam','glorious','spam']
	
	print swallow_velocity
	
	print myList
	
	print set(myList)
	
def StringStuff():
	"""
		Some stuff with strings here
	"""
	x = "Hi my name is EOK"
	
	y = x.lower()
	z = x.upper()
	
def Conditions(x):
	"""
		Simply put 0 as the parameter to
		do the recursion
	"""
	if(x == 0):
		print "First recursion x=",x
		Conditions(x+1)
	elif(x == 1):
		print "Second recursion x=",x
		Conditions(x+1)
	else:
		print "recurion completed"