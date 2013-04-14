"""
    This file contains the neccesary things to 
    know about objects in python
    
            Main things to go through are
            -Construction
            -arguements for class creation
"""
class SayMyName
	"""
		Simple Class to show how to
		create a class and use some functions
    """   
	def __init__(self, myname):
		"""
			  This is the initialiser function
			  
			  anything after self in the arguement
			  list are the real arguements
		"""
		self.myname = myname
      
    def say(self):
		"""
			As you see this function can
			use the variables held in the
		"""
		
		print "Hello ",self.myname