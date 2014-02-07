def isBouncy(n):
	return not(isInc(n) or isDec(n))

def isInc(n):
	digits = map(int, list(str(n)))
	for i in xrange(1, len(digits)):
		if digits[i-1] > digits[i]:
			return False
	return True

def isDec(n):
	digits = map(int, list(str(n)))
	for i in xrange(1, len(digits)):
		if digits[i-1] < digits[i]:
			return False
	return True

limit = 21780
bouncyCount = len(filter(isBouncy, xrange(100, limit+1)))
while True:
	limit+=1
	if isBouncy(limit):
		bouncyCount+=1
	ratio = float(bouncyCount) / float(limit)
	if ratio >= 0.99:
		print limit, ratio
		break
	
