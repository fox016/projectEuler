# Full counting sort
tests = int(raw_input())
num_str_map = {}
for test in xrange(tests):
	num, word = raw_input().split(" ")
	num = int(num)
	if test < tests / 2:
		word = "-"
	if num in num_str_map:
		num_str_map[num].append(word)
	else:
		num_str_map[num] = [word]

solution = []
for x in xrange(100):
	if x in num_str_map:
		for word in num_str_map[x]:
			solution.append(word)

print ' '.join(solution)

# Count occurrences
"""
t = int(raw_input())
nums = map(int, raw_input().split(" "))

count_map = {}
for n in nums:
        if n in count_map:
                count_map[n]+=1
        else:
                count_map[n] = 1

output = ""
for x in xrange(100):
        if x in count_map:
                output += str(count_map[x]) + " "
        else:
                output += "0 "
print output[:-1]
"""

# Sort list of numbers
"""
t = int(raw_input())
nums = map(int, raw_input().split(" "))

count_map = {}
for n in nums:
        if n in count_map:
                count_map[n]+=1
        else:
                count_map[n] = 1

output = ""
for x in xrange(t):
        if x in count_map:
                output += (str(x) + " ") * count_map[x]
print output[:-1]
"""

# Count occurrences of all less than [0-99]
"""
tests = int(raw_input())
nums = []
for test in xrange(tests):
        num, word = raw_input().split(" ")
        nums.append(int(num))

count_map = {}
for n in nums:
        if n in count_map:
                count_map[n]+=1
        else:
                count_map[n] = 1

output = ""
for x in xrange(100):
        total = 0
        for i in xrange(x+1):
                if i in count_map:
                        total += count_map[i]
        output += (str(total) + " ")
print output[:-1]
"""
