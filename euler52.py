print filter(lambda n: sorted(str(n)) == sorted(str(n*2)) == sorted(str(n*3)) == sorted(str(n*4)) == sorted(str(n*5)) == sorted(str(n*6)), xrange(1, 200000))
