def streets_nearby(segments, circles):
	for circle in circles:
		count = 0
		for seg in segments:
			data = map(int, seg.split(","))
			end1 = (data[0], data[1])
			end2 = (data[2], data[3])
			if does_contain_line(circle, end1, end2):
				print end1, end2
				count += 1
		print count

def does_contain_line(circle, end1, end2, iter=1):
	mid = ((end1[0] + end2[0]) / 2.0, (end1[1] + end2[1]) / 2.0)
	if iter == 20:
		return does_contain_point(circle, end1) or does_contain_point(circle, end2) or does_contain_point(circle, mid)
	return does_contain_line(circle, end1, mid, iter+1) or does_contain_line(circle, mid, end2, iter+1)

def does_contain_point(circle, p):
	data = map(float, circle.split(","))
	center = (data[0], data[1])
	radius = data[2]
	return get_dist(center, p) <= radius

def get_dist(p1, p2):
	delta_x = p1[0] - p2[0]
	delta_y = p1[1] - p2[1]
	return (delta_x**2 + delta_y**2)**0.5

segments = ["2,4,4,1", "2,5,5,5", "2,11,5,5", "5,5,10,5", "5,5,7,2", "5,0,7,2", "7,2,10,5"]
circles = ["5,5,10", "5,5,2", "7,3,0.6", "7,3,0.8", "6,0,2"]
segments = ["1,1,2,5", "1,1,5,4", "5,4,6,1", "6,1,1,1", "2,5,5,4"]
circles = ["3,3,2"]
streets_nearby(segments, circles)
