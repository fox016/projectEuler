def rain(m, heights):
	vol = 0
	dirty = True
	while dirty:
		dirty = False
		for index in xrange(len(heights)):
			height = heights[index]
			shortestIndex = get_smallest_neighbor(index, m, heights)
			if shortestIndex == -1:
				continue
			if heights[shortestIndex] > height:
				vol += (heights[shortestIndex] - height)
				heights[index] += (heights[shortestIndex] - height)
				dirty = True
			if heights[shortestIndex] == height:
				equal = get_equal_group(index, m, heights, set([index]))
				sides = set()
				for i in equal:
					sides |= set(get_filtered_neighbors(i, m, heights, lambda x: (heights[x] != heights[index])))
				if -1 in sides or not sides:
					continue
				smallest = min(sides, key = lambda n: heights[n])
				if heights[smallest] > height:
					for i in equal:
						vol += (heights[smallest] - height)
						heights[i] += (heights[smallest] - height)
					dirty = True
	print vol

def get_neighbors(index, m, heights):
	neighbors = list()
	if index >= len(heights):
		return neighbors
	row = index / m
	col = index % m
	if row > 0:
		neighbors.append(index-m)
	if row < (len(heights)/m)-1:
		neighbors.append(index+m)
	if col > 0:
		neighbors.append(index-1)
	if col < m-1:
		neighbors.append(index+1)
	while len(neighbors) < 4:
		neighbors.append(-1)
	return neighbors

def get_smallest_neighbor(index, m, heights):
	neighbors = get_neighbors(index, m, heights)
	if -1 in neighbors:
		return -1
	return min(neighbors, key = lambda n: heights[n])

def get_filtered_neighbors(index, m, heights, fltr):
	return filter(fltr, get_neighbors(index, m, heights))

def get_equal_group(index, m, heights, index_set):
	equal = get_filtered_neighbors(index, m, heights, lambda x: (heights[x] == heights[index]) and (x not in index_set))
	if len(equal) == 0:
		return index_set
	index_set |= set(equal)
	return_set = set()
	for i in equal:
		return_set |= get_equal_group(i, m, heights, index_set)
	return return_set

m = 3
heights = [5, 5, 5, 5, 1, 5, 5, 5, 5]
rain(m, heights)
