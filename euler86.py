import math
from fractions import gcd

def count_integer_routes(M):
	short_route_int_count = 0
	for x in xrange(1, M+1):
		for y in xrange(x, M+1):
			for z in xrange(y, M+1):
				a = z
				b = x + y
				c = math.sqrt(a**2 + b**2)
				if c == round(c):
					print (x,y,z), (a,b,c)
					short_route_int_count += 1
	return short_route_int_count

def count_from_triples(M):
	short_route_int_count = 0
	triples = generate_all_triples(100, M*3)
	for triple in triples:
		short_route_int_count += count_options(triple)
	return short_route_int_count

def count_options(triple):
	count = 0
	z = triple[0]
	x = 1
	y = triple[1] - x
	while y > z:
		y -= 1
		x += 1
	while x <= y:
		print x, y, z
		count += 1
		y -= 1
		x += 1
	z = triple[1]
	x = 1
	y = triple[0] - x
	while y > z:
		y -= 1
		x += 1
	while x <= y:
		print x, y, z
		count += 1
		y -= 1
		x += 1
	return count

def generate_primitive_triples(iter_count, max_c):
	triples = []
	for n in xrange(1, iter_count+1):
		for m in xrange(n+1, iter_count+1):
			if gcd(m, n) == 1 and (m-n) % 2 == 1 and m**2+n**2 <= max_c:
				if m**2-n**2 < 2*m*n:
					triples.append((m**2-n**2, 2*m*n, m**2+n**2))
				else:
					triples.append((2*m*n, m**2-n**2, m**2+n**2))
	return triples

def generate_all_triples(iter_count, max_c):
	triples = []
	primitives = generate_primitive_triples(iter_count, max_c)
	for triple in primitives:
		k = 1
		while k * triple[2] <= max_c:
			triples.append(map(lambda x:x*k, triple))
			k+=1
	return triples

M = 100
#print count_integer_routes(M)
#print count_from_triples(M)
print count_options((6,8,10)) # Should be 6
