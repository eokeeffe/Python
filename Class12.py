"""
	Functional programming using python
	
	Focus here is on using keywords like
	-lambda same as using it in lisp/scheme/clojure
"""

def generateNumbers(number):
	return filter(lambda x: x%5 is 0 , xrange(number))

def MappingThingsOut(string):
	return map(None,string)
	
def Reduction(list):
	return reduce(lambda x,y:x*y,list)
	
def Evaluate(string):
	return eval(string)

list = generateNumbers(int(raw_input("How many numbers needed?")))
print list

l = MappingThingsOut("Hello Kitty")
print l

# Applying filters
mylist = [2,4,6,8]
ml = Reduction(mylist)
print ml

x = 1
print Evaluate('x+1')