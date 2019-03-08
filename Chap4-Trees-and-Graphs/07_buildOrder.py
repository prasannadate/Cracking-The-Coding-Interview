class GraphNode:
	""" Graph node class

	Args:
		val: Value at node
		inEdges: Set of all inEdges 
		outEdges: Set of all outEdges

	"""

	def __init__(self, val):
		""" Initializes graph node

		Args: 
			val: Value at node

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)
		"""

		self.val = val
		self.inEdges = set()
		self.outEdges = set()




class GraphEdge:
	""" Graph edge class

	Args:
		val: Value at edge
		fromNode: Node from which edge originates
		toNode: Node at which edge terminates

	"""

	def __init__(self, val, fromNode, toNode):
		""" Initializes graph edge

		Args:
			val: Value at edge
			fromNode: Node from which edge originates
			toNode: Node at which edge terminates

		"""

		self.val = val
		self.fromNode = fromNode
		self.toNode = toNode




class Graph:
	""" Graph class

	Args:
		nodes: Set of all nodes in the graph
		edges: Set of all edges in the graph

	Methods:
		addNode(node): Adds a node to the graph
		addEdge(val, fromNode, toNode): Adds an edge to the graph

	"""

	def __init__(self):
		""" Initializes the graph

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		""" 

		self.nodes = set()
		self.edges = set()


	def __str__(self):
		nodes = []
		edges = []
		for node in self.nodes:
			nodes.append(node.val)
		for edge in self.edges:
			edges.append((edge.fromNode.val, edge.toNode.val))
		return "Nodes: " + str(nodes) + "\nEdges: " + str(edges)


	def addNode(self, node):
		""" Adds a node to the graph

		Args:
			node: Graph node to be added

		Assumptions:
			node is an object of GraphNode class

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.nodes.add(node)


	def addEdge(self, val, fromNode, toNode):
		""" Adds an edge to the graph

		Args:
			val: Value at edge
			fromNode: Node from which edge originates
			toNode: Node at which edge terminates

		Assumptions:
			fromNode and toNode are objects of GraphNode class

		"""

		edge = GraphEdge(val, fromNode, toNode)
		self.edges.add(edge)
		edge.fromNode.outEdges.add(edge)
		edge.toNode.inEdges.add(edge)




def buildOrder(projects, dependencies):
	""" Given projects and project dependencies, returns a build order

	Args:
		projects: List of projects
		dependencies: List of project dependencies

	Returns:
		A list of projects to be completed in that order

	Assumptions:
		Each element in dependencies is a tuple, where second project in the tuple
			is dependent on the first project in the tuple

	Complexity Analysis:
		Time Complexity: O(V * E), V = number of projects, E = number of dependencies
		Space Complexity: O(V + E)

	"""

	if not projects:
		return []

	G = Graph()
	nodes = {}

	for p in projects:
		nodes[p] = GraphNode(p)
		G.addNode(nodes[p])

	for start, end in dependencies:
		G.addEdge(1, nodes[start], nodes[end])

	startNodes = []
	for node in G.nodes:
		if not node.inEdges:
			startNodes.append(node)

	visited = set()
	order = []

	for startNode in startNodes:
		Q = [startNode]
		while Q:
			node = Q.pop(0)
			if node not in visited:
				addIt = True

				for edge in node.inEdges:
					if edge.fromNode not in visited:
						addIt = False
						break

				if addIt:
					visited.add(node)
					order.append(node.val)

				for edge in node.outEdges:
					if edge.toNode not in visited:
						Q.append(edge.toNode)

	if len(visited) == len(G.nodes):
		return order
	return []




# TESTING
projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
order = buildOrder(projects, dependencies)
print(order)


projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
			'n', 'o', 'p']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), \
				('g', 'h'), ('h', 'i'), ('h', 'j'), ('h', 'k'), ('i', 'l'), \
				('j', 'l'), ('k', 'm'), ('l', 'n'), ('m', 'n'), ('o', 'p'), \
				('p', 'c')]
order = buildOrder(projects, dependencies)
print(order)




































