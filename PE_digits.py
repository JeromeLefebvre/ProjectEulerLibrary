
def numberFromList(l):
	''' concantinate a number from a list '''
	return sum([a*10**(10-n-1) for n,a in enumerate(l)])

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
	return (n - n % 10**end)//10**end

def removesDigits(n,start,end):
	'''>>> removesDigits(1406357289,4,6)
	635
	>>> removesDigits(1406357289,5,7)
	357
	'''
	start -= 1
	return removeFirstnDigits( removesLastnDigits(n, numberOfDigits(n) - end), start)

def applyToDigits(n,f = None):
	''' Applies the function f to each digits and returns the sum'''
	if not f:
		f = lambda x: x
	total = 0
	while n > 0:
		total += f(n%10)
		n //= 10
	return total
	
def collatzLength_a(n,_collatz={1:1}):
	''' Computes the length of the collatz sequence and caches the result'''
	if n in _collatz:
		return _collatz[n]
	if n%2 == 0:
		_collatz[n] = collatzLength(n//2,_collatz) + 1
	else:
		_collatz[n] = collatzLength((3*n + 1)//2, _collatz) + 2
	return _collatz[n]

def collatzLength(n,_collatz={1:1,2:2,4:3}):
	''' Computes the length of the collatz sequence and caches the result'''
	''' Looking mod 4 gave only a minor increase in speed, 3%?'''
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

    def test_isPalindrome(self):
    	self.assertEqual(isPalindrome(454),True)
    	self.assertEqual(isPalindrome(44),True)

if __name__ == "__main__":
	unittest.main()