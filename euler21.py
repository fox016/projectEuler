from math import sqrt

def sumDivisors(n):
	sum = 1
	for i in xrange(2, int(sqrt(n))):
		if n % i == 0:
			sum += i
			sum += n/i
	return sum

def isAmicable(n):
	sdn = sumDivisors(n)
	return sumDivisors(sdn) == n and not sdn == n

print sum(filter(isAmicable, xrange(1,10000)))
