from fractions import gcd
from functools import reduce
from operator import mul
from fractions import Fraction
from itertools import chain, combinations

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def lcmm(args):
	"""Compute the lowest common multiple of [a,b,c,...]"""
	return reduce(lcm, args)

def gcdd(args):
	"""Compute the greatest common divisors of [a,b,c,...]"""
	return reduce(gcd, args)

def product(args):
	"""Return the products of all the elements [a,b,c,...]
	returns 1 if the list is empty"""
	return reduce(mul, args, 1)

def nCk(n,k):
    ''' Calculate nCk - the binomial coefficient'''
    return product(range(n-k+1, n+1)) // product(range(1,k+1))

def powerset(A,indices=False):
	''' powerset(set,bool) -> iterator -- returns a complete list of all subsets of A as tuple,
	if range is set to a list, returns only sets with numbers within a certain range'''
	if not indices:
		indices = range(0,len(A)+1)
	return chain.from_iterable( combinations(A,i) for i in indices )

def order(a,n):
	'''Expects (a,n) = 1, returns min k such that a^k = 1 mod n'''
	assert(gcd(a,n) == 1)
	if a == 1:
		return 1
	k = 1
	b = a
	while b % n != 1:
		b *= a
		k+= 1
	return k
	
import unittest
class TestBasicFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_gcdlcm(self):
		self.assertEqual(gcd(4,6),2)
		self.assertEqual(gcdd([4,6,8]),2)
		self.assertEqual(lcm(4,5),20)
		self.assertEqual(lcm(4,8),8)
		self.assertEqual(lcmm([4,8,12]),24)

	def test_powerset(self):
		self.assertEqual(list(powerset((1,2,3))), [(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)])
		self.assertEqual(list(powerset((1,2,3),indices=[1,2])), [(1,),(2,),(3,),(1,2),(1,3),(2,3)])

	def test_cNk(self):
		self.assertEqual(nCk(50,42), 536878650)
		self.assertEqual(nCk(1,1), 1)
		self.assertEqual(nCk(100,0), 1)
		self.assertEqual(nCk(100,10), 17310309456440)

	def test_order(self):
		self.assertEqual( order(2,7), 3)
		self.assertEqual( order(3,50), 20)
		from PE_primes import primesUpTo
		from random import randint
		# Verifying Fermat's little theorem
		primes = primesUpTo(100)
		for p in primes:
			a = randint(1,p-1)
			self.assertEqual( (p-1) % order(a,p), 0)

if __name__ == "__main__":
	unittest.main()