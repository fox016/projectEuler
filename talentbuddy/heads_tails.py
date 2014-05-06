def count_sequences(data):
	count = 0
	for target_length in xrange(1, len(data)+1):
		for start in xrange(len(data)-target_length+1):
			sub = data[start:start+target_length]
			if sub.count("H") >= len(sub) / 2.0:
				print sub
				count+=1
	print count

data = ['T', 'T', 'H', 'T']
count_sequences(data)
