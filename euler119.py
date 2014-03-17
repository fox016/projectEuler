from math import log

def sumDigits(n):
	digitSum = 0
	while n:
		digitSum, n =  digitSum + (n % 10), n / 10
	return digitSum

total = 0
limit = 10**10
margin = 10**(-10)
for x in xrange(10, limit+1):
	digitSum = sumDigits(x)
	if digitSum < 2:
		continue
	power = log(x, digitSum)
	diff = abs(power-round(power))
	if diff < margin:
		total+=1
		print total, x, digitSum, power
	if total == 30:
		break
