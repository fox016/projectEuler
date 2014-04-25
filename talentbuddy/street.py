def longest_street(segments):
	print ("%.2f" % max(map(get_length, segments)))

def get_length(segment):
	coor = map(int, segment.split(","))
	a = abs(coor[0] - coor[2])
	b = abs(coor[1] - coor[3])
	return (a**2 + b**2)**0.5

segments = ["1,1,2,5", "1,1,5,4", "5,4,6,1", "6,1,1,1", "2,5,5,4"]
longest_street(segments)
