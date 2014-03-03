

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


'''