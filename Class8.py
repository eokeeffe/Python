"""
	Dictionaries in python
	
	Works on entries
	so has a hash value (int or string) and a value that is either an
	object or a type
"""

dict = {1:"Hydrogen",2:"Helium",3:"Lithium"}
dict2 = {6:"Oxygen",7:"Nitrogen",3:"Lithium"}

#copy the dict
copy_dict = dict.copy()
#clear the dict
copy_dict.clear()
#removed the dict from memory
del copy_dict
#append to the dictionary
dict.setdefault(4, []).append("Be")
#update the value with a key value
entry = {4:'Berylium'}
dict.update(entry)

#for dealing with identical entries
d2 = [(1,'pear tree'),(5,'golden rings'),(1,'partridge')]
sort_dict = {}
for key,value in d2:
	sort_dict.setdefault(key,[]).append(value)

print dict.keys()
print dict.values()
print dict.popitem()
print dict

print "Duplicated entries dealt with",sort_dict

print "Hydrogen" in dict,"H" in dict

print dict.difference(dict2)

print dict.union(dict2)

print dict.symmetric_difference(dict2)
