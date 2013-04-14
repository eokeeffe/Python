"""
	Doctests
	This should show you how to start testing software using
	the unittest module setup
	
	So what happens here is the programmer puts the expected
	command line inputs and outputs into the doc of the function
	
	If the following examples don't evaluate correctly then the tests fail
	
	Ih they pass then run this command
	python Class14.py -v
	
	-v is for verbose so it will show exactly 
	
	in this case however all the tests should fail
"""
def Factorial(x):
	"""
	Calculate x!
	
	>>> Factorial(2)
	3
	
	>>> try: Factorial(-1)
	... except ValueError: print 'good'
	... else: print 'bzzt!'
	bzzt!
	"""
	if x < 0:
		raise ValueError("x must be positive")
	if x in (0, 1):
		return 1
	return x * Factorial(x-1)
	
def _test():
	import doctest, Class14
	doctest.testmod(Class14)
	
if __name__ == "__main__":
	_test()
