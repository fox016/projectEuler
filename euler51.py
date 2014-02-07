def generate_primes(start, limit):
	i = start
	while i <= limit:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

for p in generate_primes(100001, 1000000):
	digitCounts = [str(p).count(digit) for digit in str(p)]
	if 3 in digitCounts:
		digit = str(p)[digitCounts.index(3)]
		replacements = [int(str(p).replace(digit, str(newDigit))) for newDigit in xrange(10)]
		primeReps = filter(is_prime, replacements)
		if primeReps[0] == p and len(primeReps) == 8:
			print p
			break
