import cmath

def qRoots(a,b,c):
	# (-b)
	p1 = (-b)
	# (-b)^2 - 4ac
	p2 = (-b**2)-(4*a*c)
	# 2a
	p3 = (2*a)

	x1 = (p1 + (cmath.sqrt(p2)))/p3
	x2 = (p1 - (cmath.sqrt(p2)))/p3
	
	return x1,x2

def ParseQuadratic(string):
	x = string.Parse()
	return qRoots(x)
	
#	x^2+6x+8
#	so roots should be (x+2)(x+4)
print ParseQuadratic("x^2+6x+8")