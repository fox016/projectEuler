import sys

def my_format(n):
	string = "{0:.2f}".format(n)
	while string[-1] == "0" or string[-1] == ".":
		string = string[:-1]
	return string

def guess_last_pos(positions):
        guess = positions[0]
        for i in xrange(1,len(positions)-1):
                pos = positions[i]
                x_diff = pos[0] - guess[0]
                y_diff = pos[1] - guess[1]
                predict = (pos[0] + x_diff, pos[1] + y_diff)
                measured = positions[i+1]
                guess = ((predict[0]+measured[0])/2.0, (predict[1]+measured[1])/2.0)
        return guess

def map_matcher(segments, paths):
	for path in paths:
		positions = map(lambda pos:map(float, pos.split(",")), path.split(";"))
		last_pos = guess_last_pos(positions)
		circle = str(last_pos[0]) + "," + str(last_pos[1])
		best = (None, sys.maxint)
		for segment in segments:
			ends = map(int, segment.split(","))
			end1 = ends[0:2]
			end2 = ends[2:4]
			close_point = get_closest_point(circle, end1, end2)
			dist = get_dist(close_point, last_pos)
			if dist < best[1]:
				best = (close_point, dist)
		print my_format(best[0][0]) + "," + my_format(best[0][1])

def get_closest_point(circle, end1, end2):
	center = map(float, circle.split(","))[0:2]
	seg_v = (end2[0] - end1[0], end2[1] - end1[1])
	seg_v_mag = get_dist(end1, end2)
	pt_v = (center[0] - end1[0], center[1] - end1[1])
	unit_seg_v = map(lambda x:x/seg_v_mag, seg_v)
	proj_v = (pt_v[0] * unit_seg_v[0]) + (pt_v[1] * unit_seg_v[1])
	if proj_v < 0:
		return end1
	if proj_v > seg_v_mag:
		return end2
	proj_vec = map(lambda x:x*proj_v, unit_seg_v)
	return ((end1[0]+proj_vec[0]), (end1[1]+proj_vec[1]))

def get_dist(p1, p2):
	delta_x = p1[0] - p2[0]
	delta_y = p1[1] - p2[1]
	return (delta_x**2 + delta_y**2)**0.5

segments = ["1,1,3,1", "3,1,3,3", "3,1,5,1"]
paths = ["1,1,10;2,1.5,15;2.5,2.5,20", "1,1,10;2,1.5,15;3,1.5,20;4.2,1.5,25"]
map_matcher(segments, paths)
