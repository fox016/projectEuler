print sum(filter(lambda n: str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1], xrange(1000000)))
