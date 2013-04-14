def msplit(string, delimiters):
	'''
		Behaves str.split but supports multiple delimiters
	'''
	delimiters = tuple(delimiters)
	stack = [string,]
	for delimiter in delimiters:
		for i, substring in enumerate(stack):
			substack = substring.split(delimiter)
			stack.pop(i)
			for j, _substring in enumerate(substack):
				stack.insert(i+j, _substring)
	return stack

def mreplace(string, delimiters,replacements):
	'''
		Behaves str.replace but supports multiple delimiters
	'''
	if len(delimiters) != len(replacements):
		return []
	delimiters = tuple(delimiters)
	stack = [string,]
	for index in range(0,len(delimiters)):
		for i, substring in enumerate(stack):
			substack = substring.replace(delimiters[index],replacements[index])
			stack.pop(i)
			for j, _substring in enumerate(substack):
				stack.insert(i+j, _substring)
	return stack

def getGreatestdifference(list):
	'''
		Return the first and last index that have the
		greatest difference between terms
	'''
	print "Hello World"
	f = 0
	l = 0
	max = 0
	for index in list:
		for index2 in list:
			if index2-index > max:
				max = index2-index
				l = index2
				f = index
		return f,l,max

#list = [10,20,40,50,500]
#a,b,c = getGreatestdifference(list)
#print a,b,c
u = ['"',',','.','-','_','[',']','(',')','+','=','<','>']
v = [' " ',' , ',' . ',' - ',' _ ',' [ ',' ] ',' ( ',' ) ',' + ',' = ',' < ',' > ']
html = open("test1.htm","r").read()
file = open('t.txt','w')
#list = msplit(html,['"',',','.','-','_','[',']','(',')','+','=','<','>'])
for index in range(0,len(u)):
	html = html.replace(u[index],v[index])

list = []
for tok in html:
	list.append(tok)
for l in list:
	file.write(l)
file.close()