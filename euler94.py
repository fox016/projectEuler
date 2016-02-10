import math

#LIMIT = 1000000000
LIMIT = 1000000000
A = 0.75
B = 0.5
SOLUTION = 0

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
		return
	solutions = (-1*b + math.sqrt(root)) / (2*a), (-1*b - math.sqrt(root)) / (2*a)
	return get_solution_perimeter(solutions[0], b), get_solution_perimeter(solutions[1], b)

def get_solution_perimeter(x, b):
	if x is None or x < 0 or x != round(x) or not is_odd(x):
		return 0
	if b > 0:
		perimeter = 3*x-1
		if perimeter < LIMIT:
			print x, x-1, perimeter, SOLUTION+perimeter
			return perimeter
		return 0
	perimeter = 3*x+1
	if perimeter < LIMIT:
		print x, x+1, perimeter, SOLUTION+perimeter
		return perimeter
	return 0

for i in xrange(3, ((LIMIT+1)/3)+1):
	square = i**2
	sol1 = solve_quad(A, B, -0.25 - square)
	sol2 = solve_quad(A, -1*B, -0.25 - square)
	SOLUTION += sol1[0]
	SOLUTION += sol1[1]
	SOLUTION += sol2[0]
	SOLUTION += sol2[1]
print SOLUTION
