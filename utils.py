# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

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

	z = (b^2 - 4*a*c)
	if z == 0:
		g = -b/(2*a)
		return (g)
	elif z > 0:
		g = (-b + sqrt(z))/(2*a)
		h = (-b - sqrt(z))/(2*a)
		return (g, h)
	else:
		return None
		


def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	
	"""
	if lower <= upper:
		f= lambda x:function
		i = scipy.integrate.quad(f, lower, upper)
		return i
	
	    


	

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
