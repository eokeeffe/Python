"""
	Lists and Tuples
	
	Here we learn how to use Lists and tuples
	and also the functions these types have
"""

#	Lists are for homogeneous or same type Data-Types
#	lists for mutable objects
#	
#	Lists can act like stacks , they have the push() and pop()
#	functions 
#	
#	Lists can act like queus , they use the push(x) and pop(x)
#	x is the position in queue

#This is a list of numbers
l1 = [8,1,2,4,3,5,7,6]
#This is a list of characters
l2 = ['a','b','c','d','e','f','g','h']
#This is a list of strings
l3 = ["laser","byte","nibble","bit","dye","link","structure","carbon"]

#
#Now for some functions in Lists
#
sl1 = l1.sort()
sl2 = l2.reverse()
sl3 = l3.sort()

occurences_of_B = l3.count('b')

#
#	Tuples for data-types of the same type or the same
#	for sequence keys
#	for some functions

t1 = ('this','is','a','tuple')
t2 = [('Hello','World'),('Hello','Android'),
      ('Hello','Universe'),('These are tuples','in tuples')]
empty_tuple = ()

#Unpacking tuples

print t2

rock,paper,And,scissors = t2

print rock
print paper
print And
print scissors





