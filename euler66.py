import math
   
def getSquareRootContinuedFraction(n):
	num = 0
	den = 1
	wholeRoot = math.floor(math.sqrt(n))
	sub = wholeRoot
	cont_frac = [wholeRoot]
	while sub != wholeRoot * 2:
		num = den * sub - num
		den = (n - num**2) / den
		if den == 0:
			return 0
		sub = math.floor((wholeRoot + num) / den)
		cont_frac.append(sub)
	return cont_frac

def getP(n, cont_frac):
	if n in n_p_map:
		return n_p_map[n]
	if n == 0:
		p = cont_frac[0]
	elif n == 1:
		p = cont_frac[0] * cont_frac[1] + 1
	else:
		p = cont_frac[n] * getP(n-1, cont_frac) + getP(n-2, cont_frac)
	n_p_map[n] = p
	return p

x_d_map = {}
for d in [n for n in xrange(2, 1000+1) if n not in [x*x for x in xrange(40)]]:
	n_p_map = {}
	cont_frac = getSquareRootContinuedFraction(d)
	r = len(cont_frac) - 2
	if r % 2 == 1:
		x = getP(r, cont_frac)
	else:
		x = getP(2*r+1, cont_frac + cont_frac[1:])
	x_d_map[x] = d
	print d, x

print x_d_map[max(x_d_map.keys())]

# see http://mathworld.wolfram.com/PellEquation.html
