"""
	Passing Tuples,Lists and Dictionaries to functions
	
	also shows how to use a namespace
	
	try putting >>> mymod.math.pi
"""

# module 'mymod'
import math

def f1():
	print "No arguements here"
	
def f2(x):
	print "You passed",x
	
def f3(*list_or_tuple):
	print "list/tuple passed is:"
	for i in list_or_tuple:
		print i

def f4(a,b,c):
	print "Dictionary passed is:"
	print a,b,c
		
f1()
f2("Hello World")
f3([1,2,3,4])
dict = {"a":"Hello World","b":"Hello Universe","c":"Hello Android"}
f4(**dict)