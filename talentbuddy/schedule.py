from random import randint

def schedule_requests(req_start, req_end):
    lastEnd = 0
    count = 0
    for end, start in sorted(zip(req_end, req_start)) :    
        if start >= lastEnd :
            lastEnd = end
            count+=1
    print count

req_start = []
req_end = []
for i in xrange(50001):
	start = randint(9, 1686237)
	end = randint(start+1, 1686278)
	req_start.append(start)
	req_end.append(end)
schedule_requests(req_start, req_end)
