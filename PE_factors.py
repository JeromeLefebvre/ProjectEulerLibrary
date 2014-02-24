class orderedlist:
	def __init__(self,_ordered = []):
		self.ordered = _ordered
	
	def indexAbove(self,q):
		'''Returns the index of the largest or equal element above
		in hopefully log(n) time, n = len(self.ordered)'''
		# There is no elements greater than q in the list
		# returns an error. Maybe the better choice is to return an -1
		if q > self.ordered[-1]:
			raise IndexError
		# If it is lower than the entire list, return 0 (the rest of the algorithm breaks in any case)
		if q < self.ordered[0]: return 0
		# we now try to narrow down 
		low, high = 0, len(self.ordered) - 1
		while True:
			guess = low + (high - low)//2
			if self.ordered[guess] > q:
				high = guess
			else:
				low = guess
			# we now narrowed it enough that we only need to check one last element
			if (high - low) <= 1:
				if self.ordered[low] == q: return low
				else: return high

	def indexBelow(self,q):
		'''Returns the index of the largest or equal element above
		in hopefully log(n) time, n = len(self.ordered)'''
		# There is no elements greater than q in the list
		# returns an error. Maybe the better choice is to return an -1
		if q < self.ordered[0]:
			raise IndexError
		# If it is lower than the entire list, return 0 (the rest of the algorithm breaks in any case)
		if q > self.ordered[-1]: return len(self.ordered)-1
		# we now try to narrow down 
		low, high = 0, len(self.ordered) - 1
		while True:
			guess = low + (high - low)//2	
			if self.ordered[guess] < q:
				low = guess
			else:
				high = guess
			# we now narrowed it enough that we only need to check one last element
			if (high - low) <= 1:
				if self.ordered[high] == q: return high
				else: return low

	def __getitem__(self,pos):
		start, stop = pos.start,pos.stop
		if start > stop: return ()
		return self.ordered[self.indexAbove(start):self.indexBelow(stop)+1]
	
	def __str__(self):
		return str(self.ordered)

from operator import mul
from functools import reduce
def product(args):
	return reduce(mul, args, 1)

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return (2,3) + tuple(3*i+1|1 for i in range(1,n//3-correction) if sieve[i])

def genFactors(n):
	return generateFactors(n, orderedlist(rwh_primes2(n)),genOne=True)

def genProducts(n,numbers = [2,3]):
	return generateFactors(n, orderedlist(numbers),genOne=False)	

def generateFactors(n,primes,start=1,factors=(), genOne=False):
	'''This generates all numbers between from 1 up to n as their list of factors'''
	if genOne: yield (1,)
	if start <= n:
		for a in primes[start:n]:
			yield factors + (a,)
			for c in generateFactors(n//a,primes,a,factors+(a,)):
				yield c


# 10**5 [Finished in 0.2s]
# 10**6 [Finished in 1.2s]
# 10**7 [Finished in 10.5s]
# 10**8 [Finished in 101.4s]
# 10**9 [Finished in 988.9s]
'''
count = 0
#for a in generateFactors(10**2,orderedlist([2,3,5,7]),genOne = True):
for a in genFactors(1000):
	count += 1
print(count)

m = (-1,2,3,4,10,33,141)
l = orderedlist(m)
print(m[l.indexBelow(2)] == 2)
print(m[l.indexBelow(15)] == 10)
print(m[l.indexBelow(3)] == 3)
print(m[l.indexBelow(3)])
print(m[l.indexBelow(2200)] == 141)
print(m[l.indexAbove(4)] == 4)
print(m[l.indexAbove(10)] == 10)
print(m[l.indexAbove(1)] == 2)
print(m[l.indexAbove(5)] == 10)
print(m[l.indexAbove(4)] == 4)
print(m[l.indexAbove(2)] == 2)
print(m[l.indexAbove(140)] == 141)
print(m[l.indexAbove(0)] == 2)
print(m[l.indexAbove(-5)] == -1)
print(m[l.indexAbove(3)] == 3)
print("Testing intervals")
print(l[3:4] == (3,4))
print(l[5:11] == (10,))
print(l[4:11] == (4,10))
print(l[1:11] == (2,3,4,10))
print(l[11:1] == ())
m = (2,3,5)
l = orderedlist(m)
print(l[1:100] == (2,3,5))
print(l[3:100] == (3,5))
'''