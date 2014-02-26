
def numberFromList(l):
	''' concantinate a number from a list '''
	return sum([a*10**(len(l)-n-1) for n,a in enumerate(l)])

def isPalindrome(n):
	'''Returns True if a number is a palindrome'''
	return str(n) == str(n)[::-1]

def numberOfDigits(n):
	from math import log
	return int(log(n,10)) + 1

def removeFirstnDigits(n,start):
	'''Removes the first n digits, without converting to a string'''
	return n - (n//10**(numberOfDigits(n)-start))*10**(numberOfDigits(n)-start)

def removesLastnDigits(n,end):
	'''Removes the last n digits'''
	return (n - n % 10**end)//(10**end)

def removesDigits(n,start,end):
	'''>>> removesDigits(1406357289,4,6)
	635
	>>> removesDigits(1406357289,5,7)
	357
	'''
	#start -= 1
	return removeFirstnDigits( removesLastnDigits(n, numberOfDigits(n) - end), start)

def applyToDigits_old(n,f = lambda x: x):
	''' Applies the function f to each digits and returns the sum'''
	total = 0
	while n > 0:
		total += f(n%10)
		n //= 10
	return total

def applyToDigits(n,f = lambda x: x):
	''' Applies the function f to each digits and returns the sum'''
	return sum([f(d) for d in listFromDigits(n) ])

def listFromDigits(n):
	''' returns a list made up of the digits of n '''
	return [int(i) for i in str(n)]

def collatzLength_old(n,_collatz={1:1}):
	''' Computes the length of the collatz sequence and caches the result'''
	if n in _collatz:
		return _collatz[n]
	if n%2 == 0:
		_collatz[n] = collatzLength_old(n//2,_collatz) + 1
	else:
		_collatz[n] = collatzLength_old((3*n + 1)//2, _collatz) + 2
	return _collatz[n]

def collatzLength(n,_collatz={1:1,2:2,4:3}):
	''' Computes the length of the collatz sequence and caches the result'''
	#Looking mod 4 gave only a minor increase in speed
	if n in _collatz:
		return _collatz[n]
	if n%4 == 0:
		_collatz[n] = collatzLength(n//4,_collatz) + 2
	elif n%4 == 1:
		_collatz[n] = collatzLength((3*n+1)//4,_collatz) + 3
	elif n%4 == 2:
		_collatz[n] = collatzLength((3*(n//2) + 1)//2,_collatz) + 3
	elif n%4 == 3:
		_collatz[n] = collatzLength((3*n + 1)//2, _collatz) + 2
	return _collatz[n]

import unittest
class TestDigitFunctions(unittest.TestCase):
    def setUp(self):
    	pass

    def test_digit(self):
    	self.assertEqual(numberFromList([1,2,3]),123)
    	self.assertEqual(numberOfDigits(123456),6)
    	self.assertEqual(removeFirstnDigits(123456,2),3456)
    	self.assertEqual(removesLastnDigits(123456,2),1234)
    	self.assertEqual(removesDigits(12345678,2,6),3456)
    	self.assertEqual(removesDigits(12045678,2,6),456)
    	def f(x): return x**3
    	self.assertEqual(applyToDigits(123,f), sum([x**3 for x in [1,2,3]]))
    	self.assertEqual(applyToDigits_old(123,f), sum([x**3 for x in [1,2,3]]))
    def test_isPalindrome(self):
    	self.assertEqual(isPalindrome(454),True)
    	self.assertEqual(isPalindrome(44),True)

    def test_collatzLength(self):
    	self.assertEqual(collatzLength(500),111)
    	self.assertEqual(collatzLength_old(500),111)

if __name__ == "__main__":
	unittest.main()