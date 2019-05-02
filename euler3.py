def prime(a):
  return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

print list(filter(lambda x: prime(x) and 600851475143 % x == 0, range(3, 100000)))[-1]

"""
def prime(a):
     return not (a < 2 or any(a % x == 0 for x in range(2, int(a ** 0.5) + 1)))

highest = 0
for x in xrange(3, 100000):
	if(prime(x) and 600851475143 % x == 0):
		highest = x
print highest
"""
