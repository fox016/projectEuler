from __future__ import division

"""
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

print choose(70, 20)
print choose(60, 20) / choose(70, 20)
print 7 * (1 - (choose(60, 20) / choose(70, 20)))
"""

"""
def mult_range(high, low):
  prod = 1
  for i in xrange(low, high+1):
    prod *= i
  return prod

print 7 * (1 - (mult_range(50, 41) / mult_range(70, 61)))
"""

print 7 * (1 - (reduce(lambda x, y: x*y, xrange(41, 51), 1) / reduce(lambda x, y: x*y, xrange(61, 71), 1)))
