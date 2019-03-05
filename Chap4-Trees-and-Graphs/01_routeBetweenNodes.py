class GraphNode:
	""" Node of a graph

	Args:
		val: Value at the node
		children: Nodes of the graph to which this node is connected, in case of 
					directed graphs, children contains the outgoing edges only
		visited: Flag to keep track of whether or not this node has been visited

	"""

	def __init__(self, val):
		""" Initializes the graph node

		Args: 
			val: Value at the node

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.val = val
		self.children = set()
		self.visited = False




class Graph:
	""" Graph class

	Args:
		nodes: Set of all nodes in the graph

	Methods:
		addNode(val, children): Adds a new node to the graph with value val and 
			children children
		initVisited(): Sets visited flag in all nodes to False
		routeBetweenNodes(start, end): Checks if a route exists between start and 
			end nodes in the graph

	"""

	def __init__(self):
		""" Initializes the Graph object

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.nodes = set()


	def __str__(self):
		""" Returns a string representation of the graph
		
		Returns:
			String representation of the graph

		Complexity Analysis:
			Time Complexity: O(N^2), N = number of nodes in the graph
			Space Complexity: O(N^2), N = number of nodes in the graph

		"""

		graph = {}
		for node in self.nodes:
			childrenVals = []
			for n in node.children:
				childrenVals.append(n.val)
			graph[node.val] = childrenVals
		return str(graph)


	def addNode(self, node, children):
		""" Adds a node to the graph along with its children

		Args:
			val: Value at the node
			children: Children of the node

		Complexity Analysis:
			Time Complexity: O(children)
			Space Complexity: O(children)

		"""

		for c in children:
			node.children.add(c)

		self.nodes.add(node)


	def initVisited(self):
		""" Sets visited flag in all nodes to False

		Complexity Analysis:
			Time Complexity: O(nodes)
			Space Complexity: O(1)

		"""

		for node in self.nodes:
			node.visited = False


	def routeBetweenNodes(self, start, end):
		""" Checks if a route exists between start and end nodes in the graph

		Args:
			start: Start node
			end: End node

		Returns:
			True if route exists between start and end, False otherwise

		Complexity Analysis:
			Time Complexity: O(N^2), N = number of nodes in the graph
			Space Complexity: O(N)

		"""

		self.initVisited()

		Q = [start]

		while Q:
			node = Q.pop(0)
			node.visited = True

			if node == end:
				return True

			for n in node.children:
				if not n.visited:
					Q.append(n)

		return False





# TESTING
a = GraphNode(0)
b = GraphNode(1)
c = GraphNode(2)
d = GraphNode(3)
e = GraphNode(4)
f = GraphNode(5)

G = Graph()

G.addNode(a, [c,e])
G.addNode(b, [a])
G.addNode(c, [b])
G.addNode(d, [c])
G.addNode(e, [d])
G.addNode(f, [])

print(G)
print(G.routeBetweenNodes(a,b))
print(G.routeBetweenNodes(a,c))
print(G.routeBetweenNodes(a,d))
print(G.routeBetweenNodes(a,e))
print(G.routeBetweenNodes(b,a))
print(G.routeBetweenNodes(b,c))
print(G.routeBetweenNodes(b,d))
print(G.routeBetweenNodes(b,e))
print(G.routeBetweenNodes(c,a))
print(G.routeBetweenNodes(c,b))
print(G.routeBetweenNodes(c,d))
print(G.routeBetweenNodes(c,e))
print(G.routeBetweenNodes(d,a))
print(G.routeBetweenNodes(d,b))
print(G.routeBetweenNodes(d,c))
print(G.routeBetweenNodes(d,e))
print(G.routeBetweenNodes(e,a))
print(G.routeBetweenNodes(e,b))
print(G.routeBetweenNodes(e,c))
print(G.routeBetweenNodes(e,d))

print(G.routeBetweenNodes(f,a))
print(G.routeBetweenNodes(f,b))
print(G.routeBetweenNodes(f,c))
print(G.routeBetweenNodes(f,d))
print(G.routeBetweenNodes(f,e))
print(G.routeBetweenNodes(a,f))
print(G.routeBetweenNodes(b,f))
print(G.routeBetweenNodes(c,f))
print(G.routeBetweenNodes(d,f))
print(G.routeBetweenNodes(e,f))






























