def factorial(n):
	f = 1
	for i in xrange(1,n+1):
		f *= i
	return f

def falling_factorial(x, n):
	f = 1
	for i in xrange(n):
		f *= (x - i)
	return f

def choose(n, k):
	return falling_factorial(n, k) / factorial(k)

def calcPofN(n):
	return (2**n - n - 1) * choose(26, n)

high = 0
for i in xrange(1, 26+1):
	n = calcPofN(i)
	if n > high:
		high = n
print high

"""
# Reduced Version
import math

high = 0
for i in xrange(1, 26+1):
	n = (2**i - i - 1) * (reduce(lambda a,b: a*b, map(lambda x: 26-x, range(i)), 1) / math.factorial(i))
	if n > high:
		high = n
print high
"""
