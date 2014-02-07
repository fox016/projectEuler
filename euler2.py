def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

sum = 0
for n in fib():
	if(n > 4000000):
		print sum
		break
	if(n % 2 == 0):
		sum += n
