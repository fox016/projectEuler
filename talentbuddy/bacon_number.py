class Node:
	
	def __init__(self, value):
		self.value = value
		self.children = list()

	def addChild(self, child):
		self.children.append(child)

	def display(self, depth=0):
		print "-" * depth + self.value
		for child in self.children:
			child.display(depth+1)

class Tree:

	def __init__(self, head):
		self.head = head

	def find(self, current, value):
		if current.value == value:
			return current
		for child in current.children:
			node = self.find(child, value)	
			if node != None:
				return node
		return None

	def getNodes(self, depth, current):
		if current == None:
			return list()
		if depth <= 0:
			return list([current])
		nodeList = list()
		for child in current.children:
			nodeList += self.getNodes(depth-1, child)
		return nodeList

def list_actors(data, bacon_number):
	tree = Tree(Node("Kevin Bacon"))
	build_tree(data, tree)
#	tree.head.display()
	for actor in sorted(map(lambda node: node.value, tree.getNodes(bacon_number, tree.head))):
		print actor

def build_tree(data, tree):
	waitlist = list()
	for actors in data:
		names = actors.split(", ")
		parent = tree.find(tree.head, names[0])
		if parent != None:
			for child in names[1:]:
				parent.addChild(Node(child))
		else:
			waitlist.append(actors)
	if waitlist:
		build_tree(waitlist, tree)
	

list_actors(["Kevin Bacon, Tom Hanks, Gary Sinise, Ed Harris, Bill Paxton, Tom Cruise, Jack Nicholson, Demi Moore, Kiefer Sutherland", "Tom Cruise, Nicole Kidman, Dustin Hoffman, Val Kilmer, Meg Ryan, Billy Connolly, Ken Watanabe, Renee Zellweger, Cuba Gooding Jr.", "Nicole Kidman, Hugh Jackman, Ed Harris, Meryl Streep, Jeff Daniels, Toni Collette, Val Kilmer, Tommy Lee Jones, Jim Carrey", "Tom Hanks, Meg Ryan, Tim Allen, Michael Keaton, Jean Reno, Vin Diesel, Matt Damon, Ted Danson, Ted Danson, Sally Field, Denzel Washington", "Jeff Goldblum, Kevin Kline, William Hurt, Meg Tilly, Glenn Close, Tom Berenger, Bill Pullman, Will Smith, Vivica A. Fox, Brent Spiner", "Jack Nicholson, Michael Keaton, Kim Basinger, Helen Hunt, Cuba Gooding Jr., Diane Keaton, Keanu Reeves, Marisa Tomei, Adam Sandler", "Demi Moore, Patrick Swayze, Billy Bob Thornton, Billy Connolly, Woody Harrelson, Burt Reynolds, Jason Alexander, Jim Cummings", "Brent Spiner, Patrick Stewart, Jonathan Frakes, LeVar Burton, Michael Dorn, Gates McFadden, Marina Sirtis, James Cromwell", "Kiefer Sutherland, Charlie Sheen, Chris O'Donnell, Tim Curry, Sandra Bullock, Matthew McConaughey, Samuel L. Jackson, Julia Roberts", "Dustin Hoffman, Robin Williams, Julia Roberts, Sharon Stone, Samuel L. Jackson, Liev Schreiber, Angelina Jolie, Jack Black, Jackie Chan", "Meg Ryan, Billy Crystal, Carrie Fisher, Tim Robbins, Stephen Fry, Nicolas Cage, Sam Neill, Hugh Grant, Robert Downey Jr., Jean Reno", "Sam Neill, Jeff Goldblum, Richard Attenborough, Samuel L. Jackson, Wayne Knight, Sean Connery, Alec Baldwin, James Earl Jones, Tim Curry"], 6)
