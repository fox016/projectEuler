class Node:

        def __init__(self, id, value):
                self.id = id
                self.value = value
                self.borders = set()

        def addBorder(self, other):
                self.borders.add(other)
                other.borders.add(self)

class Graph:

        def __init__(self):
                self.nodes = {}

        def addNode(self, id, value):
                self.nodes[id] = Node(id, value)

        def addEdge(self, source_id, sink_id):
                self.nodes[source_id].addBorder(self.nodes[sink_id])

	def getSubgraphValue(self, init_id, ignore_id):
		open = [init_id]
		visited = set()
		value = 0
		while open:
			node_id = open.pop(0)
			node = self.nodes[node_id]
			value += node.value
			visited.add(node_id)
			for border in node.borders:
				if border.id in visited or border.id == ignore_id:
					continue
				open.append(border.id)
		return value

size = int(raw_input())
graph = Graph()
initValue = 0
for id, value in zip(range(1,size+1), map(int, raw_input().split(" "))):
        graph.addNode(id, value)
	initValue += value
edges = []
for edge in xrange(size-1):
        source, sink = map(int, raw_input().split(" "))
        edges.append((source, sink))
        graph.addEdge(source, sink)
diffs = set()
for edge in edges:
        diff = abs(initValue - (2 * graph.getSubgraphValue(edge[0], edge[1])))
	diffs.add(diff)
print min(diffs)
