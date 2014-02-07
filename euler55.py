def isLynchrel(n, iter=0):
	sum = n + int(str(n)[::-1])
	if str(sum) == str(sum)[::-1]:
		return False
	if iter > 50:
		return True
	return isLynchrel(sum, iter+1)

print len(filter(isLynchrel, xrange(10, 10000)))
