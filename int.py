from scipy.integrate import quad

def integrate(function, lower, upper):
	if lower <= upper:
		f= lambda x:eval(function)
		i = quad(f, lower, upper)
		return i[0]