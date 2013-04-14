"""
	Doctests
	This should show you how to start testing software using
	the unittest module setup
	
	So here we can see that we the tests have passed
"""
def Factorial(x):
	"""
	Calculate x!
	
	>>> Factorial(2)
	2
	>>> Factorial(4)
	24
	
	"""
	if x < 0:
		raise ValueError("x must be positive")
	if x in (0, 1):
		return 1
	return x * Factorial(x-1)
	
def _test():
	import doctest, Class15
	doctest.testmod(Class15)
	
if __name__ == "__main__":
	_test()
