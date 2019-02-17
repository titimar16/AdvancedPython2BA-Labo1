from math import *
from scipy.integrate import quad

def fact(n):

	if n < 0:
		raise ValueError()
	z = 1
	for i in range(1,n+1):
		z = z * i
	return z
	



def roots(a, b, c):

	z = (b**2 - 4*a*c)
	if z == 0:
		g = -b/(2*a)
		return (g)
	elif z > 0:
		g = (-b - sqrt(z))/(2*a)
		h = (-b + sqrt(z))/(2*a)
		return (g, h)
	else:
		return None
		


def integrate(function, lower, upper):
	if lower <= upper:
		f= lambda x:eval(function)
		i = quad(f, lower, upper)
		return i[0]
	
	    


	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))

print(integrate('x ** 2 - 1', -1, 1))