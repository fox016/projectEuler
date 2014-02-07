def generate_primes(limit):
	yield 2
	yield 3
	i = 5
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

primes = [p for p in generate_primes(700000)]
print "Primes Generated."

for j in xrange(400, 600):
	for i in xrange(len(primes)-j):
		total = sum(primes[k] for k in xrange(i, i+j))
		if total >= 1000000:
			break
		if is_prime(total):
			print "%s, %s, %s" % (total, j, primes[i])
