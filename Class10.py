"""
	OOP style programming in python
	covering 
	-Inheritance
	-Operator interception and overloading
"""

import sqlite3 as lite

class Nametag:
	"""
		This forms a basic template for all other inherited
		classes
		i.e becomes a superclass
	"""
	def __init__(self,myname):
		#instance variable created
		self.myname = myname
	def say(self):
		print "Hello , my name is",self.myname
	def __str__(self):
		return self.myname
		
# Creating a class that inherits from another

class GamerTag(Nametag):
	"""
		This class when iniated will call the Nametag
		__init__ function
		
		The say() function is overided from the Nametag class
		i.e is now a subclass
	"""
	def say(self):
		print "The current value of my name is",self.myname
		
	def WhoAmI(self):
		print self.myname
		
# Example of Mulitple Inheritance 

class PersistentNameTag(Nametag,GamerTag):
	def save(self):
		self.test = None
		try:
			self.test = lite.connect('test.db')
			cur = self.test.cursor()
			cur.execute('SELECT SQLITE_VERSION()')
			cur.execute("CREATE TABLE Names(Id INT,Name TEXT)")
			cur.execute("INSERT INTO Names VALUES(1,self.myname)")
			data = cur.fetchone()
			print "SQLite version: %s" % data
		except lite.Error, e:
			print "Error %s:" % e.args[0]
		finally:
			if self.test:
				self.test.close()

class Employee:
	def __init__(self,firstname):
		self.fn = firstname
	def __iter__(self):
		X = []
		for i in range(1 10):
			X.append(i)
		return X
	def __repr__(self):
		return self.fn
	def __setattr__(self):
		X = 1
	def __setitem__(self):
		X = 1
	def __str__(self):
		return self.fn
				
me = PersistentNameTag("Evan")

me.say()
me.WhoAmI()
me.save()