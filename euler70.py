from fractions import gcd

def phi(n):
	count = 1
	for x in xrange(2, n):
		if gcd(n, x) == 1:
			count+=1
	return count

def isPermutation(n1, n2):
	return sorted(list(str(n1))) == sorted(list(str(n2)))

for n in xrange(2, 10000000):
	if isPermutation(n, phi(n)):
		print n, phi(n)
