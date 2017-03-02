import math

# NOT 312530630458602039
# NOT 138907096
# YES 518408346

LIMIT = 1000000000
   
def get_square_root_cont_frac(n):
	num = 0
	den = 1
	whole_root = math.floor(math.sqrt(n))
	sub = whole_root
	cont_frac = [whole_root]
	while sub != whole_root * 2:
		num = den * sub - num
		den = (n - num**2) / den
		if den == 0:
			return 0
		sub = math.floor((whole_root + num) / den)
		cont_frac.append(sub)
	return cont_frac

# x**2 - 3y**2 = 1
# x = ((a (+|-) 1) / 2)
# y = h

D = 3

d_root = get_square_root_cont_frac(D)
p = d_root[0] * d_root[1] + 1
q = d_root[1]

for n in xrange(10):
	x = ((p + (q * math.sqrt(D)))**n + (p - (q * math.sqrt(D)))**n) / 2
	y = ((p + (q * math.sqrt(D)))**n - (p - (q * math.sqrt(D)))**n) / (2 * math.sqrt(D))
	a1, a2 = 2*x+1, 2*x-1
	b1, b2 = 2 * math.sqrt(a1**2 - y**2), 2 * math.sqrt(a2**2 - y**2)
	print a1, b1
	print a2, b2

# see euler66.py
