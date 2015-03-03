import random

solutions = []

for i in xrange(1000000):

	digits = "0123456789"
	plates = set()
	count = 0

	while True:
		new_plate = int(random.choice(digits) + random.choice(digits) + random.choice(digits))
		count += 1
		if (1000 - new_plate) in plates:	
			solutions.append(count)
			break
		plates.add(new_plate)

print float(sum(solutions)) / len(solutions)
