from functools import reduce
from fractions import Fraction
def nCk(n,k):
	return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def binomialCoeff(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result
 
from operator import mul
def comb(n,r):
    ''' calculate nCr - the binomial coefficient
    >>> comb(3,2)
    3
    >>> comb(9,4)
    126
    >>> comb(9,6)
    84
    >>> comb(20,14)
    38760
    '''
    if r > n-r:  # for smaller intermediate values
        r = n-r
    return int( reduce( mul, range((n-r+1), n+1), 1) /
      reduce( mul, range(1,r+1), 1) )   

from cProfile import run
if __name__ == "__main__":
    run("[nCk(n,k) for n in range(1,150) for k in range(1,150)]") # 32.324 seconds
    run("[binomialCoeff(n,k) for n in range(1,150) for k in range(1,150)]") # 0.385 seconds
    run("[comb(n,k) for n in range(1,150) for k in range(1,150)]") # 0.110 seconds