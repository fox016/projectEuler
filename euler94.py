import math

#LIMIT = 1000000000
LIMIT = 10000
A = 0.75
B = 0.5

def is_square(num):
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

"""
solution = 0
for x in xrange(3, (LIMIT/3)+3, 2):
	solution += test_triangle(x, x-1)
	solution += test_triangle(x, x+1)
print solution
"""

# NOT 312530630458602039
# NOT 138907096
# YES 518408346

def solve_quad(a, b, c):
	root = b**2 - (4*a*c)
	if root < 0:
		return None, None
	return (-1*b + math.sqrt(root)) / (2*a), (-1*b - math.sqrt(root)) / (2*a)

def is_int(x):
	if x is None:
		return False
	return x == round(x)

def print_ints(x1,x2,x3,x4):
	if is_int(x1): print x1
	if is_int(x2): print x2
	if is_int(x3): print x3
	if is_int(x4): print x4

for i in xrange(((LIMIT/3)+3)**2):
	square = i**2
	x1,x2 = solve_quad(A, B, 0.25 - square)
	x3,x4 = solve_quad(A, -1*B, 0.25 - square)
	print_ints(x1,x2,x3,x4)
