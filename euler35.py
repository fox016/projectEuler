from collections import deque

def is_prime(n):
	if n < 4:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

def isCircularPrime(n):
	if not is_prime(n):
		return False
	numQ = deque(str(n))
	for i in xrange(len(str(n))-1):
		numQ.rotate(1)
		if not is_prime(int(''.join(numQ))):
			return False
	return True

print len(filter(isCircularPrime, xrange(2, 1000000)))
