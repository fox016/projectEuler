import collections

"""
size = int(raw_input())
nums = collections.deque(map(int, raw_input().split(" ")))
"""

nums = collections.deque(range(10**4))

best = 0
for i in xrange(len(nums)):
	total = sum(map(lambda n, add: n*add, nums, xrange(1,len(nums)+1)))
	if total > best:
		best = total
	nums.rotate(1)
print best
