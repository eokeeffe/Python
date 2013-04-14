from operator import itemgetter
f = open("list.txt","r")
l = []
for line in f.readlines():
	#print line
	li = line.strip('\n').split(',')
	l.append(list((int(li[0]),int(li[1]))))
f.close()
#print len(l)
i=0
j=0
l2 = []
for part in l:
	print part
	
l = sorted(l, key=itemgetter(1))
print "-----------"
for part in l:
	print part
while i < len(l)/2:
	l2.append((l[i],l[(len(l)-1)-i]))
	i += 1
	j -= 1
print "-----------"
for part in l2:
	print part