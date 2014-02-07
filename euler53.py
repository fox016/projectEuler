from math import factorial

def choose(n, r): return factorial(n) / (factorial(r) * factorial(n-r))
print len(filter(lambda num: num > 1000000, [choose(n, r) for n in xrange(1, 101) for r in xrange(1, n+1)]))
