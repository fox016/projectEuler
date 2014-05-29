size = int(raw_input())
nums = map(int, raw_input().split(" "))
best = 0
for start in xrange(len(nums)):
	total = 0
	for add in xrange(len(nums)):
		total += (nums[(start+add) % len(nums)] * (add+1))
	if total > best:
		best = total
print best
