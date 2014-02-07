def generate_primes():
	yield 2
	yield 3
	i = 5
	while True:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

prod = 1
for p in generate_primes():
	next = prod * p
	if next > 1000000:
		print prod
		break
	prod = next
