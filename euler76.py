values = xrange(1, 100)
target = 100
table = [1] + [0] * target
for value in values:
	for i in xrange(value, target+1):
		table[i] += table[i-value]
print table[target]
