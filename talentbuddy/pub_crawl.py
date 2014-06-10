import sys

class Node:
	
	def __init__(self, value):
		self.value = value
		self.edges = {}

	def __str__(self):
		node = str(self.value) + ":"
		for e in self.edges:
			edge = self.edges[e]
			node += "(" + str(edge[0].value) + ", " + str(edge[1]) + ") "
		return node
	
	def __repr__(self):
		return self.__str__()

	def addEdge(self, sink, weight):
		self.edges[sink.value] = (sink, weight)

class Graph:

	def __init__(self, city_map):
		self.nodes = {}
		for edge in city_map:
			source, sink, weight = map(int, edge.split(","))
			self.addEdge(source, sink, weight)

	def __str__(self):
		graph = ""
		for value in self.nodes:
			graph += self.nodes[value].__str__() + "\n"
		return graph
	
	def __repr__(self):
		return self.__str__()

	def size(self):
		return len(self.nodes)

	def getNode(self, value):
		if value in self.nodes:
			return self.nodes[value]
		return None

	def addEdge(self, source_value, sink_value, weight):
		source = self.getNode(source_value)
		if not source:
			source = Node(source_value)
			self.nodes[source_value] = source
		sink = self.getNode(sink_value)
		if not sink:
			sink = Node(sink_value)
			self.nodes[sink_value] = sink
		source.addEdge(sink, weight)

	def traverse(self, start_value):
		open = [(start_value, 0, 1)]
		while open:
			open = sorted(open, key = lambda o: o[1])
			value, cost, visited = open.pop(0)
			node = self.getNode(value)
			if visited >= self.size():
				if start_value in node.edges:
					return (float(cost) + node.edges[start_value][1]) / visited
			for e in node.edges:
				edge = node.edges[e]
				nextNode, weight = edge
				open.append((nextNode.value, cost+weight, visited+1))

def get_best_tour(city_map):
	graph = Graph(city_map)
	best = sys.maxint
	for val in graph.nodes:
		cost = graph.traverse(val)
		print cost
		if cost < best:
			best = cost
	print "{0:.3f}".format(best)[:-1]

#city_map = ["1,2,1","2,3,1","1,3,1","3,4,2","4,1,3"]
#city_map = ["10,9,1", "9,2,2", "2,10,4", "2,7,2", "7,9,4", "7,6,2", "6,2,3", "7,10,13", "4,5,16", "5,10,16", "5,4,14", "8,8,14", "3,5,14", "7,3,12", "5,2,15", "3,6,12", "7,4,12", "3,1,15", "4,2,12", "3,8,15", "3,7,12", "9,8,14", "8,4,16", "9,3,13", "9,9,16", "3,3,15", "5,9,16", "1,4,16", "4,6,13", "1,10,15", "6,5,14", "4,7,13", "8,5,15", "5,6,12", "10,2,12", "6,7,14", "2,8,12"]
#city_map = ["6,2,3", "2,1,4", "1,6,1", "1,4,4", "4,2,2", "4,10,4", "10,1,2", "2,6,13", "8,9,13", "5,6,12", "6,8,16", "5,7,16", "6,9,14", "11,8,16", "9,3,12", "9,8,12", "10,9,16", "4,11,15", "2,7,16", "2,9,13", "3,7,14", "7,2,12", "11,4,12", "10,3,16", "11,6,14", "9,9,13", "6,11,15", "1,1,12", "4,1,12", "4,8,14", "10,5,12", "3,1,14", "2,2,14", "8,1,15", "9,7,16", "5,4,13", "11,11,16", "7,8,14", "10,7,13", "7,11,12"]
city_map = ["10,11,1", "11,6,2", "6,10,3", "6,2,3", "2,11,4", "2,12,2", "12,6,2", "12,7,3", "7,2,1", "6,11,16", "7,8,12", "11,9,13", "8,4,12", "11,3,14", "5,8,14", "9,5,14", "1,9,12", "2,10,15", "5,9,14", "12,5,14", "5,7,13", "4,9,14", "2,2,16", "7,9,15", "4,10,12", "4,7,15", "5,11,15", "9,6,14", "6,8,16", "3,7,16", "8,5,13", "7,7,12", "8,3,14", "8,7,13", "4,8,13", "8,12,15", "3,2,16", "10,6,12", "10,3,13", "7,11,14", "2,7,15", "1,2,16", "3,3,12", "9,7,15", "6,1,12"]

get_best_tour(city_map)
