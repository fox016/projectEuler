A_INIT = -9.8
V_INIT = 0.0
EARTH_RADIUS = 6371000.0
DELTA_T = 0.01 # Smaller DELTA_T increases accuracy, but increases runtime -- O(1/n)

total_distance = 0.0
total_time = 0.0
a = A_INIT
v = V_INIT

while total_distance < EARTH_RADIUS:
	d = abs((v * DELTA_T) + (0.5 * a * DELTA_T * DELTA_T))
	v += (a * DELTA_T)
	total_distance += d
	total_time += DELTA_T
	a = (1 - (total_distance / EARTH_RADIUS)) * A_INIT

print "{0} minutes".format((total_time * 2) / 60.0)
