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

count = 1
for p in generate_primes():
	if(count == 10001):
		print p	
		break
	count+=1
