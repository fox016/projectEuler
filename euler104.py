from math import log10

def isPandigital(n):
	return sorted(n) == ['1','2','3','4','5','6','7','8','9']

fib_1 = 1
fib_2 = 1
n = 3
while True:
	if n % 1000 == 0: print n
	current = fib_1 + fib_2
	tail = current % 1000000000
	if isPandigital(str(tail)):
		length = 1 + int(log10(current))
		if length > 9:
			head = current / 10**(length-9)
			if isPandigital(str(head)):
				print n
				break
	fib_1 = fib_2
	fib_2 = current
	n+=1
