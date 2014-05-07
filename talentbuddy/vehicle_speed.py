def vehicle_speed(positions):
	for i in xrange(1, len(positions)):
		data1 = map(int, positions[i-1].split(","))
		p1 = (data1[0], data1[1])
		t1 = data1[2]
		data2 = map(int, positions[i].split(","))
		p2 = (data2[0], data2[1])
		t2 = data2[2]
		print "{0:.2f}".format(get_dist(p1, p2) / (t2 - t1))
        
def get_dist(p1, p2):
	delta_x = p1[0] - p2[0]
	delta_y = p1[1] - p2[1]
	return (delta_x**2 + delta_y**2)**0.5

positions = ["1,1,10", "3,1,20", "4,1,30", "4,4,35"]
vehicle_speed(positions)
