def count_requests(requests, pro_start, pro_end):
	requests = sorted(requests)
	for i in xrange(len(pro_start)):
		count = 0
		startIndex = findFirstGTE(requests, pro_start[i])
		endIndex = findLastLTE(requests, pro_end[i])
		print endIndex - startIndex + 1

def findFirstGTE(data, val):
	index = binarySearch(data, val)[0]
	if data[index] < val:
		while index < len(data) and data[index] < val:
			index+=1
		return index
	while index >= 0 and data[index] >= val:
		index-=1
	return index+1
	
def findLastLTE(data, val):
	index = binarySearch(data, val)[1]
	if data[index] > val:
		while index >= 0 and data[index] > val:
			index-=1
		return index
	while index < len(data) and data[index] <= val:
		index+=1
	return index-1

def binarySearch(data, val):
	highIndex = len(data)-1
	lowIndex = 0
	while highIndex > lowIndex:
		index = (highIndex + lowIndex) / 2
		sub = data[index]
		if data[lowIndex] == val:
			return [lowIndex, lowIndex]
		elif sub == val:
			return [index, index]
		elif data[highIndex] == val:
			return [highIndex, highIndex]
		elif sub > val:
			if highIndex == index:
				return sorted([highIndex, lowIndex])
			highIndex = index
		else:
			if lowIndex == index:
				return sorted([highIndex, lowIndex])
			lowIndex = index
	return sorted([highIndex, lowIndex])

requests = range(0, 50000)
pro_start = [1] * 50000
pro_end = [50000] * 50000
count_requests(requests, pro_start, pro_end)
