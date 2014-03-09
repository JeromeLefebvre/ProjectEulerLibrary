from memoize import memoize

def fib2(n,_fib={}):
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

@memoize
def fib(n):
    from math import sqrt
    ''' This is the fibonacci squence starting from 1,1,2,3,5,...'''
    # There are even faster ways of computing this, see: http://en.literateprograms.org/Fibonacci_numbers_(Python)
    # pass n == 71, the accuracy drops enough that you start to generate errors.
    if n < 72:
        return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    else:
        return fib(n-1) + fib(n-2)

def test_order(orderFunc):
    primes = primesUpTo(10000)
    for p in primes:
        a = randint(1,p-1)
        orderFunc(a,p)

from cProfile import run
if __name__ == "__main__":
    run("[fib(i) for i in range(1,100000)]")  # 2.321
    run("[fib2(i) for i in range(1,100000)]") # 2.481 seconds