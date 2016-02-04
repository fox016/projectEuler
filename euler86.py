import math
from fractions import gcd

def count_from_triples(M):
	short_route_int_count = 0
	triples = generate_all_triples(100, M*3)
	for triple in triples:
		short_route_int_count += count_abc_options(triple, M)
	return short_route_int_count

def count_abc_options(triple, M):
	return count_xyz_options(1, triple[1]-1, triple[0], M) + count_xyz_options(1, triple[0]-1, triple[1], M)

def count_xyz_options(x, y, z, M):
	if z > M:
		return 0
	count = 0
	if y > z:
		x, y = x+y-z, z
	if x <= y:
		count += ((y-x)/2) + 1
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

M = 1818
print count_from_triples(M)
