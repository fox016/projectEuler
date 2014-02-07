"""
def generate_primes(limit):
	yield 2
	yield 3
	i = 5
	while i<= limit:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

def is_permutation(n1, n2, n3):
	return ''.join(sorted(str(n1))) == ''.join(sorted(str(n2))) == ''.join(sorted(str(n3)))

def is_sequence(n1, n2, n3):
	return (n3 - n2 == n2 - n1)

primes = [p for p in generate_primes(10000) if p > 1000] # All 4-digit primes

for i in xrange(len(primes)):
	for j in xrange(i+1, len(primes)):
		for k in xrange(j+1, len(primes)):
			if is_sequence(primes[i], primes[j], primes[k]):
				if is_permutation(primes[i], primes[j], primes[k]):
					print "{0}, {1}, {2}".format(primes[i], primes[j], primes[k])
"""

import time
tStart = time.time()
from math import ceil, sqrt
from itertools import permutations

# Generate primes using sieve method
def primes(limit):
    set_primes = set(xrange(3, limit, 2))
    for i in xrange(3, int(ceil(sqrt(limit))), 2):
        if i in set_primes:
            multiples_of_i = set(xrange(2 * i, limit, i))
            set_primes -= multiples_of_i
    set_primes.add(2)
    return set_primes
    
set_of_primes = primes(10000)
found = False

for i in xrange(1000, 10000):
    if i in set_of_primes and i != 1487:
        perms = [int("".join(p)) for p in permutations(str(i))]
        prime_perms = set(filter(lambda x: x in set_of_primes and x > i, perms))
        if len(prime_perms) >= 2:
            for j in sorted(list(prime_perms)):
                k = 2 * j - i
                if k in prime_perms:
                    print "%s%s%s" % (i, j, k)
                    found = True
                    break
    if found:
        break        
        

print "Run Time = " + str(time.time() - tStart)
