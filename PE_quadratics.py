

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

import unittest
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass
	def test_solving(self):
		# Thest a bunch of values for the isSquare function
		from random import randint
		for i in range(1,2000):
			d = randint(1,10**100)
			self.assertEqual(isSquare(d**2),d)

		# (x + a)(x + b) = x**2 + (a+b)x + ab
		for a in range(-100,100):
			for b in range(-100,100):
				solns = [-a,-b]
				solns.sort()
				self.assertEqual(solveIntegerQuadratic(1,a+b,a*b),solns)
		# x**2 + 1 = 0 has no solutions
		self.assertEqual(solveIntegerQuadratic(1,0,1), [])        
		# x + 2 = 0 has one solutions
		self.assertEqual(solveIntegerQuadratic(0,1,2), [-2])
		# 2x + 1 = 0 has no solutions
		self.assertEqual(solveIntegerQuadratic(0,2,1), [])
		for e in range(-10,10):
			for f in range(-10,10):
				for a in range(-10,10):
					for b in range(-10,10):
						if a*b*e*f != 0:
							solns = solveIntegerLinear(e,a) + solveIntegerLinear(f,b)
							solns.sort()
							self.assertEqual(solveIntegerQuadratic(e*f,f*a+e*b,a*b),solns)

		triangles = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]
		for i in range(-10,121):
			if isTriangle(i):
				self.assertEqual( i in triangles, True)
			else:
				self.assertEqual( i in triangles, False)

from math import sqrt
def pell(d):
	'''This uses the Chakravala method:
	http://en.wikipedia.org/wiki/Chakravala_method
	Returns the minimum solution'''
	p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
	while k != 1 or y == 0:
		p = k * (p//k+1) - p
		p = p - int((p - sd)//k) * k
		x = (p*x1 + d*y) // abs(k)
		y = (p*y + x1) // abs(k)
		k = (p*p - d) // k
		x1 = x
	return x
	
if __name__ == '__main__':
	unittest.main()