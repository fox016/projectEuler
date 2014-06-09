def getArea(polygon):
	xList = []
	yList = []
	for point in polygon:
		x, y = point.split(",")
		xList.append(int(x))
		yList.append(int(y))
	sum1 = 0
	sum2 = 0
	for i in xrange(len(xList)):
		sum1 += xList[i] * yList[(i+1)%len(yList)]
		sum2 += yList[i] * xList[(i+1)%len(xList)]
	return abs(0.5 * (sum1 - sum2))

def getAreas(polygon, point):
	total = 0
	for start in xrange(len(polygon)-1):
		total += getArea(polygon[start:start+2] + [point])
	total += getArea([polygon[-1], polygon[0], point])
	return total

def count_trips(neighborhood, trips):
	count = 0
	n_size = getArea(neighborhood)
	for trip in trips:
		innersize = getAreas(neighborhood, trip)
		if innersize == n_size:
			count+=1
	print count

neighborhood = ["1,3", "4,5", "3,1"]
trips = ["1,1", "2,3", "3,3", "4,2"]
count_trips(neighborhood, trips)
