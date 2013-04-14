"""
	Class on how to deal with exceptions in python
	
	3 things to remember
	-try
	-catch
	-finally
"""
		
def HowToUseExceptions(filename):
	f = open(filename)
	try:
		data = f.read()
	except IOError:
		data = None
	finally:
		f.close()
		print "As the stream isn't being used any more we have to close it"
		print "Exception means I need to start again or Shutdown"
		print "So Goodbye"
	return data
		
HowToUseExceptions("Data.txt")