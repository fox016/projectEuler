def generate_primes():
	yield 2
	yield 3
	i = 5
	while True:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

sum = 0
for p in generate_primes():
	if(p < 2000000):
		sum += p
	else:
		break
print sum
