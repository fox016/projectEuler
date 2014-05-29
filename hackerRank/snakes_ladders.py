class Node:

	def __init__(self, value):
		self.value = value
		self.sinks = set()

	def addSink(self, sink):
		self.sinks.add(sink)

	def getSinks(self):
		return self.sinks

	def display(self):
		print self.value, "=>", sorted(map(lambda n: n.value, self.sinks))
		print ""

class Graph:

	def __init__(self):
		self.nodes = {}
		
	def addNode(self, value):
		if value not in self.nodes:
			self.nodes[value] = Node(value)
		return self.nodes[value]

	def getNode(self, value):
		return self.nodes[value]

	def addEdge(self, sourceValue, sinkValue):
		self.nodes[sourceValue].addSink(self.nodes[sinkValue])

	def findDepth(self, value, start):
		q = [(0, start)]
		while q:
			obj = q.pop(0)
			depth = obj[0]
			node = obj[1]
			if node.value == value:
				return depth
			for sink in node.getSinks():
				obj = (depth+1, sink)
				if obj not in q:
					q.append(obj)
		return -1

	def display(self):
		print ""
		print "-------"
		print "Graph"
		print "-------"
		for n in self.nodes:
			self.nodes[n].display()

def isStart(n, paths):
	return n in map(lambda p: int(p[0]), paths)

def getEnd(n, paths):
	for path in paths:
		if int(path[0]) == n:
			return int(path[1])

def getBestPath(ladders, snakes):
	size = 100
	graph = Graph()
	futureEdges = []
	for n in xrange(size, 0, -1):
		graph.addNode(n)
		if isStart(n, ladders+snakes):
			continue
		for x in xrange(1,6+1):
			if n + x > size:
				break
			elif isStart(n+x, ladders):
				graph.addEdge(n, getEnd(n+x, ladders))
			elif isStart(n+x, snakes):
				futureEdges.append((n, getEnd(n+x, snakes)))
			else:
				graph.addEdge(n, n+x)
	for edge in futureEdges:
		graph.addEdge(edge[0], edge[1])
	print graph.findDepth(100, graph.getNode(1))

tests = int(raw_input())
for test in xrange(tests):
	ladderCount, snakeCount = map(int, raw_input().split(","))
	ladders = map(lambda x: x.split(","), raw_input().split(" ")) # bottom-to-top
	snakes = map(lambda x: x.split(","), raw_input().split(" ")) # mouth-to-tail
	getBestPath(ladders, snakes)
