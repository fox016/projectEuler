class Node:

	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
		self.parent = None

	def setRight(self, right):
		self.right = right
		right.parent = self

	def setLeft(self, left):
		self.left = left
		left.parent = self

class Tree:

	def __init__(self, head):
		self.head = head

	# Returns number of leaf nodes in tree
	def countLeaves(self, node=None):

		if node is None:
			node = self.head

		if node.right is None and node.left is None:
			return 1

		rightLeaves = 0
		leftLeaves = 0

		if node.left != None:
			leftLeaves = self.countLeaves(node.left)
		if node.right != None:
			rightLeaves = self.countLeaves(node.right)
		
		return rightLeaves + leftLeaves

	# Returns number of nodes along path (from head to child) with given value
	def countPathValue(self, child, value):

		if child is None:
			return 0

		if child.value == value:
			return 1 + self.countPathValue(child.parent, value)
		return self.countPathValue(child.parent, value)

	# Recursively builds binary tree
	def addNode(self, value, parent, size):
		
		newNode = Node(value)
		if parent.left is None:
			parent.setLeft(newNode)
		elif parent.right is None:
			parent.setRight(newNode)
		else:
			print "Cannot add third child"
			exit(1)

		if self.countPathValue(newNode, "d") < size:
			self.addNode("d", newNode, size)
		if self.countPathValue(newNode, "r") < size:
			self.addNode("r", newNode, size)

head = Node("head")
tree = Tree(head)

size = 10 

tree.addNode("r", head, size)

print tree.countLeaves() * 2
