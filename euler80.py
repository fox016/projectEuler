from decimal import *

getcontext().prec=100

"""
total = 0
for n in xrange(1, 100):
	numStr = str(Decimal(n) ** Decimal('0.5'))[2:]
	total += sum(map(int, list(numStr)))
print total
"""

print sum(map(int, list(''.join([str(Decimal(n) ** Decimal('0.5'))[2:] for n in xrange(1, 100)]))))
