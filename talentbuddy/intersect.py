from math import ceil

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
	line1 = get_line(coor1[0], coor1[1], coor1[2], coor1[3])
	line2 = get_line(coor2[0], coor2[1], coor2[2], coor2[3])
	intersect = get_intersection(line1, line2)
	if intersect['x'] == None:
		return False
	return is_on_line(intersect, line1) and is_on_line(intersect, line2)

def is_on_line(point, line):
	point['x'] = ceil(point['x'])
	point['y'] = ceil(point['y'])
	if (point['x'] >= line['x1'] and point['x'] <= line['x2']) or (point['x'] <= line['x1'] and point['x'] >= line['x2']):
		if (point['y'] >= line['y1'] and point['y'] <= line['y2']) or (point['y'] <= line['y1'] and point['y'] >= line['y2']):
			return True
	return False

def get_line(x1, y1, x2, y2):
	m, b = None, None
	if x1 == x2:
		return {"m": m, "b": b, "x1": x1, "x2": x2, "y1": y1, "y2": y2}
	if x1 == 0:
		b = y1
	elif x2 == 0:
		b = y2
	else:
		b = (y1 * (x2 / x1) - y2) / ((x2 / x1) - 1)
	if x1 == 0:
		m = (y2 - b) / x2
	else:
		m = (y1 - b) / x1
	return {"m": m, "b": b, "x1": x1, "x2": x2, "y1": y1, "y2": y2}

def get_intersection(line1, line2):
	x, y = None, None
	if line1['m'] == line2['m']:
		return {"x": x, "y": y}
	if line1['m'] == None:
		x = line1['x1']
		y = line2['m'] * x + line2['b']
		return {"x": x, "y": y}
	if line2['m'] == None:
		x = line2['x1']
		y = line1['m'] * x + line1['b']
		return {"x": x, "y": y}
	if line1['m'] == 0:
		y = line1['b']
	elif line2['m'] == 0:
		y = line2['b']
	else:
		y = ((line2['m'] / line1['m']) * line1['b'] - line2['b']) / ((line2['m'] / line1['m']) - 1)
	if line1['m'] == 0:
		x = (y - line2['b']) / line2['m']
	else:
		x = (y - line1['b']) / line1['m']
	return {"x": x, "y": y}

segments = ["0,1,2,1", "1,0,1,2"]
intersecting_segments(segments)
