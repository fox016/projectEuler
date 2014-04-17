def get_value(tree, index):
	if index > len(tree):
		return "*"
	return tree[index-1]

def depth_first(tree):
	solution = list()
	traverse(tree, 1, solution)
	print ''.join(solution)

def traverse(tree, index, solution):
	value = get_value(tree, index)
	if value == "*":
		return
	traverse(tree, 2*index, solution)
	solution.append(value)
	traverse(tree, 2*index+1, solution)
	
depth_first("puvetnarynapl ieu issklnl a eetNv,nra rmtc,ae eigi daateot m g.***e* *d***n*c*c***a*e* *** *s*e*** *l*a*** *x*i***n*h*s***n*h**")
