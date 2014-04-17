def get_ends(dependencies, heads, tails):
	for d in dependencies:
		if "*" in d:
			continue
		nodes = d.split(',')
		heads.add(nodes[0])
		tails.add(nodes[1])

def print_set(s):
	for item in s:
		print item

def print_lone_elements(dependencies):
	lone = set()
	for d in dependencies:
		nodes = d.split(',')
		if nodes[0] != "*":
			lone.add(nodes[0])
		if nodes[1] != "*":
			lone.add(nodes[1])
	print_set(lone)

def update_dependencies(dependencies, first, last):
	newDependencies = list()
	for d in dependencies:
		nodes = d.split(',')
		head = nodes[0]
		tail = nodes[1]
		for f in first:
			if head == f:
				head = "*"
			if tail == f:
				tail = "*"
		for l in last:
			if head == l:
				head = "*"
			if tail == l:
				tail = "*"
		if head == "*" and tail == "*":
			continue
		newDependencies.append(head + "," + tail)
	return newDependencies

def topological_sort(dependencies):
	heads = set()
	tails = set()
	ends = get_ends(dependencies, heads, tails)
	first = heads - tails
	last = tails - heads
	print_set(first)
	if not heads and not tails:
		print_lone_elements(dependencies)
		print_set(last)
		return
	topological_sort(update_dependencies(dependencies, first, last))
	print_set(last)

topological_sort(["keep,on" , "keep,calm" , "calm,and" , "calm,carry", "carry,on"])
topological_sort(["0,11", "0,14", "0,5", "1,2", "10,12", "11,9", "12,7", "13,5", "14,13", "2,6", "2,8", "3,8", "3,8", "4,10", "5,4", "6,14", "6,3", "6,8", "8,0", "9,14"])
