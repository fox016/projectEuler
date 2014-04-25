def intersecting_segments(segments):
	counts = [0] * len(segments)
	for first in xrange(len(segments)):
		for second in xrange(first+1, len(segments)):
			if is_intersecting(segments[first], segments[second]):
				counts[first]+=1
				counts[second]+=1
	for count in counts:
		print count

def is_intersecting(seg1, seg2):
	coor1 = map(float, seg1.split(","))
	coor2 = map(float, seg2.split(","))
	point1 = [coor1[0], coor1[1]]
	point2 = [coor1[2], coor1[3]]
	point3 = [coor2[0], coor2[1]]
	point4 = [coor2[2], coor2[3]]
	return point1 == point3 or point1 == point4 or point2 == point3 or point2 == point4

segments = ["0,1,2,1", "1,0,1,2"]
intersecting_segments(segments)
