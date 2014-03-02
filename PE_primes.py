
def _try_composite(a, d, n, s):
	if pow(a, d, n) == 1:
		return False
	for i in range(s):
		if pow(a, 2**i * d, n) == n-1:
			return False
	return True # n  is definitely composite
 
def isPrime(n, _precision_for_huge_n=16):
	''' Returns True if n is a prime number '''
	# This is the so called RabinMiller prime factorization
	if n in (0,1):
		return False
	if n in _known_primes:
		return True
	if any((n % p) == 0 for p in _known_primes):
		return False
	d, s = n - 1, 0
	while not d % 2:
		d, s = d >> 1, s + 1
	# Returns exact according to http://primes.utm.edu/prove/prove2_3.html
	if n < 1373653: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3))
	if n < 25326001: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
	if n < 118670087467: 
		if n == 3215031751: 
			return False
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
	if n < 2152302898747: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
	if n < 3474749660383: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
	if n < 341550071728321: 
		return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
	# otherwise
	return not any(_try_composite(a, d, n, s) 
				   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if isPrime(x)]

def brent(N):
	from random import randint
	from fractions import gcd
	if N%2==0:
		return 2
	y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
	g,r,q = 1,1,1
	while g==1:             
		x = y
		for i in range(r):
			y = ((y*y)%N+c)%N
		k = 0
		while (k<r and g==1):
			ys = y
			for i in range(min(m,r-k)):
				y = ((y*y)%N+c)%N
				q = q*(abs(x-y))%N
			g = gcd(q,N)
			k = k + m
		r = r*2
	if g==N:
		while True:
			ys = ((ys*ys)%N+c)%N
			g = gcd(abs(x-ys),N)
			if g>1:
				break
	return g    

def factorize(n, _d={0:[],1:[],2:[2]}):
	''' factorize returns any n number as a list of factors '''
	args = n
	if n in _d: return _d[n]
	factors = []
	while n != 1:
		q = brent(n)
		n //= q
		if isPrime(q):
			factors += [q]
		else:
			factors += factorize(q)
		if n in _d:
			factors += _d[n]
			break
	_d[args] = factors
	return factors

def primesUpTo(n):
	""" Input n>=6, Returns a list of primes, 2 <= p < n """
	# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
	# This is the so called rwh_primes2 algorithm
	correction = (n%6>1)
	n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
	sieve = [True] * (n//3)
	sieve[0] = False
	for i in range(int(n**0.5)//3+1):
		if sieve[i]:
			k=3*i+1|1
			sieve[ ((k*k)//3)::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
			sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
	return (2,3) + tuple(3*i+1|1 for i in range(1,n//3-correction) if sieve[i])



from PE_basic import powerset,product
def divisors(n):
	if type(n) == type(0):
		return {product(a) for a in powerset(factorize(n))}
	if type(n) in [type(()), type(set())]:
		return {product(a) for a in powerset(n)}

def sigma(n,power=1,proper = False):
	''' Returns the sum of all divisors or of all proper divisors'''
	if power == 1 and proper == True:
		return d(n)	
	offset = 0
	div = divisors(n)
	if proper:
		offset = -max(div)
	if power == 0:
		return len(div)
	return sum([f**power for f in div]) + offset

def d(n):
	''' A fast version of sigma(n,1), does not currently work for large n>10**30'''
	m, sigma = n ** 0.5, 1
	# If n is a square, the algorithm will be overcounting it
	if m == int(m): sigma -= int(m)
	m = int(m) + 1
	for i in range(2, m):
		# For every divisor, we get a pair
		if n%i == 0: sigma += i + (n//i)
	return sigma	

from itertools import combinations
def divisorsFromFactors(factors):
	'''Given a set of number as a set of factors, return a set of all divisors'''
	divisors = [1]
	for numDiv in range(1,len(factors)+1):
		for c in combinations(factors, numDiv):
			divisors.append(product(c))
	return set(divisors)

	
def iPrime(start=0, step=1):
	''' count(start=0, step=1) --> count object
	Return a count object whose .__next__() method returns consecutive primes values'''
	from itertools import count
	D = {}  # map each composite integer to its first-found prime factor
	# To speed things up, we deal with 2 as a special case
	if 2 >= start:
		yield 2
	for q in count(3,2):     # q gets 3, 5, 7, ... ad infinitum
		p = D.pop(q, None)
		if p is None:
			# q not a key in D, so q is prime, therefore, yield it
			if q >= start and q % step == 0:
				yield q
			# mark q squared as not-prime (with q as first-found prime factor)
			D[q*q] = q
		else:
			# let x <- smallest (N*p)+q which wasn't yet known to be composite
			# we just learned x is composite, with p first-found prime factor,
			# since p is the first-found prime factor of q -- find and mark it
			x = p + q
			while x in D or x % 2 == 0:
				x += p
			D[x] = p

import unittest
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		pass

	def test_primesUpTo(self):
		self.assertEqual(primesUpTo(10),(2,3,5,7))

	def test_brent(self):
		self.assertEqual(brent(101),101)

	def test_isPrime(self):
		self.assertEqual(isPrime(59649589127497217),True)
	def test_factorize(self):
		# 0 and 1 are special cases
		self.assertEqual(factorize(0), [])
		self.assertEqual(factorize(1), [])
		# Let's check the first few fermat numbers
		self.assertEqual(factorize(2**1 + 1), [3])
		self.assertEqual(factorize(2**(2**1) + 1), [5])
		self.assertEqual(factorize(2**(2**2) + 1), [17])
		self.assertEqual(factorize(2**(2**3) + 1), [257])
		self.assertEqual(factorize(2**(2**4) + 1), [65537])
		self.assertEqual(factorize(2**(2**5) + 1), [641,6700417])
		self.assertEqual(factorize(2**(2**6) + 1), [274177,67280421310721])
		#self.assertEqual(factorize(2**(2**7) + 1), [59649589127497217,5704689200685129054721])
	def test_primes(self):
		primes = primesUpTo(10**6)
		for index,p in enumerate(iPrime()):
			self.assertEqual(p,primes[index])
			if index == len(primes)-1:
				break
		
	def test_divisors(self):
		self.assertEqual(divisors(6), {1, 2, 3, 6})
		self.assertEqual(divisors(60),{1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30,60})
		self.assertEqual(divisors(1260), {1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15, 18, 20, 21, 28, 30, 35, 36, 42, 45, 60, 63, 70, 84, 90, 105, 126, 140, 180, 210, 252, 315, 420, 630, 1260})
		self.assertEqual(sum(divisors(1260)),4368)

	def test_sigma(self):
		self.assertEqual(sigma(3421,0),4)
		self.assertEqual(sigma(3421,1),3744)
		self.assertEqual(sigma(3421,1,proper=True),323)
		self.assertEqual(sigma(184092,1,proper=False),464520)
		self.assertEqual(sigma(184092,1,proper=True),280428)

if __name__ == '__main__':
	unittest.main()