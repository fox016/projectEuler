def count_subsets(n):
	print fib(n+1)

fibs = {0:1, 1:1}
def fib(x):
	if x in fibs:
		return fibs[x]
	mod = 524287
	if x % 2 == 0:
		n = x/2
		fibs[x] = (fib(n)**2 + fib(n-1)**2) % mod
		return fibs[x]
	else:
		n = (x-1)/2
		fibs[x] = (fib(n) * (2 * fib(n-1) + fib(n))) % mod
		return fibs[x]

n = 1000000000
count_subsets(n)
