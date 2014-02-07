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

def is_twice_square(n):
	return ((n/2)**0.5)%1 == 0

primes = [p for p in generate_primes(5000)]

for n in xrange(9, 10000, 2):
	if is_prime(n):
		continue
	isSum = False
	for p in primes:
		if p > n:
			break
		if is_twice_square(n-p):
			isSum = True
			break
	if not isSum:
		print n
		break
