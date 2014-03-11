"""
limit = 1000
total = 0
for a in xrange(3, limit+1):
	mods = []
	for n in xrange(1, 2*a+1, 2):
		mods.append(((a-1)**n + (a+1)**n) % a**2)
	total += max(mods)
	print total
print total
"""

print sum(2*a*((a-1)/2) for a in xrange(3, 1001))
