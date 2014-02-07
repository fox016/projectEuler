def generate_primes():
	yield 2
	yield 3
	i = 5
	while True:
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

def getConsecutivePrimeCount(a, b):
	n = 0
	while is_prime(n**2 + a*n + b):
		n+=1
	return n
	
best_a = 0
best_b = 0
best_sol = 0
for b in generate_primes():
	if b >= 1000:
		break
	for a in xrange(-999, 0):
		n = getConsecutivePrimeCount(a, b)
		if n > best_sol:
			best_a = a
			best_b = b
			best_sol = n
print "a: {0}".format(best_a)
print "b: {0}".format(best_b)
print "n: {0}".format(best_sol)
print "Product: {0}".format(best_a * best_b)
