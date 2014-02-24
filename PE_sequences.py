
import unittest 


def triangle(n):
	''' Returns the sum of the first n integers, expects the solution to be an integer'''
	# We expect a positive integers, anything else and the program calling this function made an error
	assert(n >= 0)
	return n*(n+1)//2

phi = (1 + 5**(1/2))/2

def fib(n,_fib={}):
	from math import sqrt
	''' This is the fibonacci squence starting from 1,1,2,3,5,...'''
	# There are even faster ways of computing this, see: http://en.literateprograms.org/Fibonacci_numbers_(Python)
	if n not in _fib:
		# pass n == 71, the accuracy drops enough that you start to generate errors.
		if n < 72:
			_fib[n] = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
		else:
			_fib[n] = fib(n-1) + fib(n-2)
	return _fib[n]


def sumOfSquares(n):
	'''Returns the sums of squares of the first n integers'''
	assert(n>= 0)
	return n*(n+1)*(2*n + 1)//6

############################################################################
########### Various iterator
############################################################################

def iFibonacci():
	''' An interator for the Fibonacci sequence 1,2,3,5'''
	a,b = 1,1
	while True:
		yield b
		a,b = b, a+b


from itertools import count

def iPentagonal(max=10**1000):
	n = 1
	while (n*(3*n - 1)/2) < max:
		yield n*(3*n - 1)//2
		n += 1

def iPentagonal(maxn=10**1000):
	for n in count():
		yield n*(3*n - 1)//2
		if n > maxn:
			return False

def iHexagonal(max=10**1000):
	n = 1
	while n*(2*n-1) < max:
		yield n*(2*n-1)
		n += 1

def iTriangle(max=10**1000):
	n = 1
	while (n*(n+1)//2) < max:
		yield n*(n+1)//2
		n += 1

def iSquare(max=10**1000):
	n = 1
	while n**2 < max:
		yield n**2
		n += 1

def iHeptagonal(max=10**1000):
	n = 1
	while n*(5*n - 3)//2 < max:
		yield n*(5*n -3)//2
		n += 1

def iOctagonal(max=10**1000):
	n = 1
	while n*(3*n - 2) < max:
		yield n*(3*n - 2)
		n += 1

def iCube(max=10**1000):
	n = 1
	while n**3 < max:
		yield n**3
		n += 1		

def isTriangle(a):
	''' I.e. is there a solutin to a = n*(n+1)/2 in the positive integers?'''
	return any(n >= 0 for n in solveIntegerQuadratic(1,1,-2*a))

def isPentagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(3,-1,-2*a))

def isHexagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(2,-1,-a))

def isHeptagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(5,-3,-2*a))

def isOctagonal(a):
	return any(n > 0 for n in solveIntegerQuadratic(3,-2,-a))

def isSquare(a):
	'''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
	# If a is a small number, then we can do this quick version
	if 0 <= a <= 2**50:
		sr = int(a**(1/2))
		if sr**2 == a:
			return sr
	# If a is large number, due to loss of precision, we use a purely integer solution, which is slower
	else:
		# Our first guess is that x is 'halfway' between 0 and n
		x = a
		y = (x + a // x) // 2
		while y < x:
			# Here we take the average between x and a//x and this becomes out new x
			# with this, at every step x and a//x both approach the square root of n
			# x from above, a//x from below
			# y stands for the previous step
			x = y
			y = (x + a // x) // 2
		if x**2 == a:
			return x

def solveIntegerLinear(a,b):
	''' solveIntegerLinear(int, int) -> list -- Returns the integer solution to ax + b = 0 or an empty list'''
	# all integers are solutions to 0x = 0
	# so there is no good outputs to this
	if a == 0 and b == 0:
		raise ValueError
	if -b % a == 0:
		return [-b//a]
	return []

def solveIntegerQuadratic(a,b,c):
	''' solveIntegerQuadratic(int,int,int) -> list -- Returns a list (sorted by size and possibly empty) of all possible integer roots (with multiplicity)  to the quadratic polynomial of the form ax^2 + bx + c'''
	# Note, this is now a pure integer solution
	# If a is zero, then we simply have a linear polynomial
	if a == 0:
		return solveIntegerLinear(b,c)
	disc = b**2 - 4*a*c # The usual discriminant
	soln = []
	# We take the integer square of the disc
	sd = isSquare(disc)
	# We need to worry about the zero solution as 0 == False in python
	if sd == 0 or sd:
		# The two possible solutions
		if (-b - sd) % (2*a) == 0:
			soln.append((-b - sd) // (2*a))
		if (-b + sd) % (2*a) == 0:
			soln.append((-b + sd) // (2*a))
	soln.sort()
	return soln

def isSquare(a):
	'''isSquare(int) -> int --  Returns the square root of a if a is a square in the positive integers, None otherwise'''
	# If a is a small number, then we can do this quick version
	if 0 <= a <= 2**50:
		sr = int(a**(1/2))
		if sr**2 == a:
			return sr
	# If a is large number, due to loss of precision, we use a purely integer solution, which is slower
	else:
		# Our first guess is that x is 'halfway' between 0 and n
		x = a
		y = (x + a // x) // 2
		while y < x:
			# Here we take the average between x and a//x and this becomes out new x
			# with this, at every step x and a//x both approach the square root of n
			# x from above, a//x from below
			# y stands for the previous step
			x = y
			y = (x + a // x) // 2
		if x**2 == a:
			return x


def isTriangle(a):
	'''isTriangle(int) -> bool -- True if there is a solution to a = n*(n+1)/2 in the positive integers'''
	return any(n >= 0 for n in solveIntegerQuadratic(1,1,-2*a))
	
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_triangle(self):
		self.assertEqual(triangle(0),0)
		self.assertEqual(triangle(10),sum(range(10+1)))
		self.assertRaises(AssertionError,triangle,-1)

	def test_fib(self):
		with open("Fib_data.txt","r") as FibonacciData:
			fib_test = {}
			for n in FibonacciData.readlines():
				key,value = n.split(':')
				fib_test[int(key)] = int(value)

		for i in range(1,200):
			self.assertEqual(fib(i),fib_test[i])

if __name__ == '__main__':
	unittest.main()

