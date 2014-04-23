def count_palind(s):
	total = 0
	for length in xrange(1, len(s)+1):
		for start in xrange(len(s)-length+1):
			sequence = s[start:start+length]
			print sequence
			if sequence == sequence[::-1]:
				total+=1
	print total

s = "abaaac"
count_palind(s)
