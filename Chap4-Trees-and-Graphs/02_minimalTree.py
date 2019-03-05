class BinaryTreeNode:
	""" Node of a binary tree

	Args:
		val: Value at the node
		left: Left subtree of the node
		right: Right subtree of the node

	"""

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


	def __str__(self):
		""" String representation of this node

		Returns:
			String representation of this node

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in the tree
			Space Complexity: O(N)

		"""

		return str(self.bfs()[:-1])


	def bfs(self):
		""" Returns breadth first search representation of the tree

		Returns:
			Breadth first search representation of the tree

		Complexity Analysis: 
			Time Complexity: O(N), N = number of nodes in the tree
			Space Complexity: O(N)

		"""

		Q = [[self]]
		bfsTree = []
		while Q:
			currq = Q.pop(0)
			nextq = []
			level = []
			while currq:
				q = currq.pop(0)
				if q is None:
					level.append(None)
				else:
					level.append(q.val)
					nextq.append(q.left)
					nextq.append(q.right)
			if nextq:
				Q.append(nextq)
			if level:
				bfsTree.append(level)
		return bfsTree




def minimalTree(vals):
	""" Creates a binary search tree from a increasingly sorted list

	Args:
		vals: Increasingly sorted list

	Returns:
		BinaryTreeNode which is the root of the resulting tree

	Complexity Analysis:
		Time Complexity: O(N), N = length of vals
		Space Complexity: O(N)

	"""

	if not vals:
		return None

	mid = len(vals) // 2
	root = BinaryTreeNode(vals[mid])
	root.left = minimalTree(vals[:mid])
	root.right = minimalTree(vals[mid+1:])

	return root





# TESTING
vals = [1,2,3,4,5,6,7,8]
print(minimalTree(vals))
















