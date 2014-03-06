from decimal import *
getcontext().prec=105

print sum(map(int, list(''.join([str(Decimal(n).sqrt()).replace('.', '')[:100] for n in xrange(1, 100) if n not in [j*j for j in xrange(10)]]))))
