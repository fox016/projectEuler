total = 0
for exp in xrange(1, 50):
	expCount = 0
	for base in xrange(1, 10):
		n = str(base**exp)
		if len(n) == exp:
			expCount+=1
		if len(n) > exp:
			break
	total += expCount
print total
