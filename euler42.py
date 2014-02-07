"""
def generate_triangles(max):
	n = 1
	t_n = 1
	while t_n <= max:
		yield t_n
		n+=1
		t_n = int(0.5 * n * (n + 1))

triangles = set([t for t in generate_triangles(200)])
"""

print len(filter(lambda word: ((((sum(["ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(c)+1 for c in word])*8+1)**0.5)-1)/2)%1==0 , [line.split(",") for line in open("files/42.dat", 'r')][0]))

