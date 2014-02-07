print sum(filter(lambda n: sum([int(d)**5 for d in str(n)]) == n, xrange(2, 1000000)))

# OR 
# print sum([n for n in xrange(2, 1000000) if sum([int(d)**5 for d in str(n)]) == n])
