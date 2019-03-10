class BinaryTreeNode:
	""" Binary tree node

	Args:
		val: Value at node
		left: Left subtree 
		right: Right subtree

	"""

	def __init__(self, val):
		""" Initializes the binary tree node object

		Args:
			val: Value at node

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.val = val
		self.left = None
		self.right = None


	def __str__(self):
		""" String representation of tree object

		Returns:
			String representation of tree object

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in the tree
			Space Complexity: O(N)

		"""

		Q = [self]
		vals = []

		while Q:
			node = Q.pop(0)
			if node:
				vals.append(node.val)
				Q.append(node.left)
				Q.append(node.right)
			else:
				vals.append(None)

		return str(vals)




def pathsWithSum(root, target):
	""" Counts number of paths going from parent to chilren in the tree starting
			at root such that the paths sum to target

	Args:
		root: Root node of the tree
		target: Sum target

	Returns:
		Number of paths summing up to target

	Complexity Analysis:
		Time Complexity: O(Nlog(N)), N = number of nodes in the tree
		Space Complexity: O(N)

	"""

	if not root:
		return 0

	pathCount = 0
	Q = [root]

	while Q:
		node = Q.pop(0)
		pathSums = pathSumsStartingAt(node)

		for s in pathSums:
			if s == target:
				pathCount += 1

		if node.left:
			Q.append(node.left)

		if node.right:
			Q.append(node.right)

	return pathCount




def pathSumsStartingAt(root):
	""" Finds sum of all paths starting at the root node 

	Args:
		root: Root node of the tree

	Returns:
		List containing sums of all paths starting at root and going downwards

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in the tree
		Space Complexity: O(N)
	
	"""

	if not root:
		return []

	leftSums = pathSumsStartingAt(root.left)
	rightSums = pathSumsStartingAt(root.right)

	return [root.val] + [root.val + v for v in leftSums] + \
		[root.val + v for v in rightSums]




# TESTING
Tree = BinaryTreeNode(0)
Tree.left = BinaryTreeNode(-1)
Tree.right = BinaryTreeNode(1)
Tree.left.left = BinaryTreeNode(2)
Tree.left.right = BinaryTreeNode(-2)
Tree.right.left = BinaryTreeNode(-2)
Tree.right.right = BinaryTreeNode(2)

print(Tree)

print(pathsWithSum(Tree, -3))
print(pathsWithSum(Tree, -2))
print(pathsWithSum(Tree, -1))
print(pathsWithSum(Tree, 0))
print(pathsWithSum(Tree, 1))
print(pathsWithSum(Tree, 2))
print(pathsWithSum(Tree, 3))
























