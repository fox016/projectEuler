def generate_primes():
	yield 2
	yield 3
	i = 5
	while True:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	if n < 4:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

def is_truncatable(n):
	if n < 10:
		return False
	truncLeft = str(n)
	while len(truncLeft) > 1:
		truncLeft = truncLeft[1:]
		if not is_prime(int(truncLeft)):
			return False
	truncRight = str(n)
	while len(truncRight) > 1:
		truncRight = truncRight[0:-1]
		if not is_prime(int(truncRight)):
			return False
	return True

count = 0
truncatable = []
for p in generate_primes():
	if count == 11:
		break
	if is_truncatable(p):
		truncatable.append(p)
		count+=1
print sum(truncatable)
