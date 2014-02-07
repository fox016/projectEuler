from math import factorial

print sum(filter(lambda n: sum(map(factorial, [int(d) for d in str(n)])) == n, xrange(3, 45000)))
