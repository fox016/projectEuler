def isReversible(n):
	if n % 10 == 0:
		return False
	if n > 10000 and n < 100000:
		return False
	for digit in map(int, str(n + int(str(n)[::-1]))):
		if digit % 2 == 0:
			return False
	return True

limit = 100000000
count = 0
for n in xrange(10, limit):
	if isReversible(n):
		count += 1
print limit, count
