import math

LIMIT = 1000000000

def is_square(num):
	"""
	x = num // 2
	seen = set([x])
	while x * x != num:
		x = (x + (num // x)) // 2
		if x in seen:
			return False
		seen.add(x)
	return True
	"""
	root = long(math.sqrt(num))
	return root**2==num

def is_odd(num):
	return num % 2 == 1

def test_triangle(x, y):
	root = x**2 - (0.5 * y)**2
	if not is_square(root):
		return 0
	perimeter = 2 * x + y
	print x, y, perimeter
	return perimeter

solution = 0
for x in xrange(3, (LIMIT/3)+3, 2):
	solution += test_triangle(x, x-1)
	solution += test_triangle(x, x+1)
print solution

# NOT 312530630458602039
# NOT 138907096
# YES 518408346
