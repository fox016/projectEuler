def getBestPath(ladders, snakes):
	pass

tests = int(raw_input())
for test in xrange(tests):
	ladderCount, snakeCount = map(int, raw_input().split(","))
	ladders = raw_input().split(" ") # bottom-to-top
	snakes = raw_input().split(" ") # mouth-to-tail
	getBestPath(ladders, snakes)
