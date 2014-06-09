class Node:

	def __init__(self, a, b, name):
		self.a = a
		self.b = b
		self.name = name
		self.parent = None

	def __str__(self):
		if self.parent:
			return self.parent.__str__() + "\n" + self.name
		return self.name

	def __repr__(self):
		return self.__str__()

	def setParent(self, parent):
		self.parent = parent

class Graph:

	def __init__(self):
		self.nodes = {}

	def addNode(self, parent, a, b, name):
		if (a, b) in self.nodes:
			return None
		sink = Node(a, b, name)
		self.nodes[(a, b)] = sink
		sink.setParent(parent)
		return sink

def pour_water(target, a_cap, b_cap):
	graph = Graph()
	open = [Node(0, 0, "")]
	found = False
	while open:
		node = open.pop(0)
		if node.a == target or node.b == target:
			found = True
			print node
			break
		edges = []
		edges.append(graph.addNode(node, a_cap, node.b, "fill A"))
		edges.append(graph.addNode(node, node.a, b_cap, "fill B"))
		edges.append(graph.addNode(node, 0, node.b, "empty A"))
		edges.append(graph.addNode(node, node.a, 0, "empty B"))
		if node.a <= b_cap - node.b:
			edges.append(graph.addNode(node, 0, node.b + node.a, "pour A into B"))
		else:
			edges.append(graph.addNode(node, node.a - (b_cap - node.b), b_cap, "pour A into B"))
		if node.b <= a_cap - node.a:
			edges.append(graph.addNode(node, node.a + node.b, 0, "pour B into A"))
		else:
			edges.append(graph.addNode(node, a_cap, node.b - (a_cap - node.a), "pour B into A"))
		for edge in edges:
			if edge:
				open.append(edge)
	if not found:
		print "impossible"
	

target = 700
a_cap = 850
b_cap = 35
pour_water(target, a_cap, b_cap)
