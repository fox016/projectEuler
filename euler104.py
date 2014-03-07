def isEndPandigital(n):
	return ''.join(sorted(n[-9:])) == "123456789"

def isStartPandigital(n):
	return ''.join(sorted(n[:9])) == "123456789"

fib = [0,1,1]
n = 3
while True:
	if n % 1000 == 0: print n
	fib.append(fib[n-1] + fib[n-2])
	currentStr = str(fib[n])
	if len(currentStr) >= 9 and isEndPandigital(currentStr) and isStartPandigital(currentStr):
		print n
		break
	n+=1
