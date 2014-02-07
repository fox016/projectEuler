from math import factorial

print sum([int(digit) for digit in str(factorial(100))])

print sum(map(int, str(factorial(100))))
