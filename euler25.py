def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

index = 1
for n in fib():
	if len(str(n)) >= 1000:
		print index
		exit(0)
	index += 1
