from fractions import gcd

count = 0
for denom in xrange(2, 12001):
	for num in xrange(1, denom):
		if float(num) / float(denom) <= 1.0/3.0:
			continue
		if float(num) / float(denom) >= 1.0/2.0:
			break
		if gcd(num, denom) == 1:
			count += 1
print count
