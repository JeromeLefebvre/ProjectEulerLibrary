from functools import reduce
from fractions import Fraction

from PE_primes import phi, primesUpTo
from fractions import gcd
from random import randint
def order(a,n):
    ''' Find the order of the integer n modulo the integer m'''
    assert(gcd(a,n) == 1)
    eulerPhi = phi(n)
    a %= n
    for d in range(1,eulerPhi+1):
        if eulerPhi % d == 0:
            if (a**d - 1) % n == 0:
                return d

def order2(a,n):
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

def test_order(orderFunc):
    primes = primesUpTo(10000)
    for p in primes:
        a = randint(1,p-1)
        orderFunc(a,p)

from cProfile import run
if __name__ == "__main__":
    run("test_order(order)")  # 1.460 seconds
    run("test_order(order2)") # 54.197 seconds