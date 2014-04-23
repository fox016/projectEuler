
def skyscrapers(heights):
	vol = 0
	tallLeftIndex = 0
	tallRightIndex = max(xrange(2, len(heights)), key = lambda x: heights[x]) 
	for index in xrange(1, len(heights)-1):
		if index == tallRightIndex:
			tallRightIndex = max(xrange(index+1, len(heights)), key = lambda x: heights[x])
		smallIndex = min(tallLeftIndex, tallRightIndex, key = lambda x: heights[x])
		if heights[smallIndex] > heights[index]:
			vol += (heights[smallIndex] - heights[index])
		if heights[index] > heights[tallLeftIndex]:
			tallLeftIndex = index
	print vol

heights = [9,8,7,8,9,5,6]
skyscrapers(heights)
