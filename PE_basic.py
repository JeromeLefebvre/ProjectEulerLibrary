from fractions import gcd
from functools import reduce
from operator import mul
from fractions import Fraction

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

def powerset(A,nonTrivial=False):
	''' powerset(set) -> iterator -- returns a complete list of all subsets of A as tuple, if nonTrivial=True, returns all set expects the empty set and A'''
	from itertools import chain, combinations
	if nonTrivial:
		return chain.from_iterable( combinations(A,i) for i in range(1,len(A)) )
	else:	
		return chain.from_iterable( combinations(A,i) for i in range(0,len(A)+1) )

def order(a,n):
	'''Expects (a,n) = 1, returns min k such that a^k = 1 mod n'''
	k = 1
	while a**k % n != 1:
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

	def test_powerset(self):
		self.assertEqual(list(powerset((1,2,3))), [(),(1,),(2,),(3,),(1,2),(1,3),(2,3),(1,2,3)])
		self.assertEqual(list(powerset((1,2,3),True)), [(1,),(2,),(3,),(1,2),(1,3),(2,3)])

	def test_cNk(self):
		self.assertEqual(nCk(50,42), 536878650)
		self.assertEqual(nCk(1,1), 1)
		self.assertEqual(nCk(100,0), 1)
		self.assertEqual(nCk(100,10), 17310309456440)

if __name__ == "__main__":
	unittest.main()