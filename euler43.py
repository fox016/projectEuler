from itertools import permutations

primes = [2, 3, 5, 7, 11, 13, 17]

def isSubDivisible(n):
	global primes
	for start in xrange(1, 8):
		if int(str(n)[start:start+3]) % primes[start-1] != 0:
			return False
	return True

print sum(filter(isSubDivisible, [int(''.join(pan)) for pan in permutations("0123456789")]))
