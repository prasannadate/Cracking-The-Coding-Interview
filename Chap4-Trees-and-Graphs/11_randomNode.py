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




class BinaryTree:
	""" Binary tree class

	Args:
		root: Root node of the tree
		numNodes: Number of nodes in the tree

	Methods:
		insert(val): Inserts a new node with value val
		find(val): Finds if a node with value val exists in the tree
		getRandomNode(self): Returns a random node from the tree
		delete(val): Deletes a node with value val

	"""

	def __init__(self):
		""" Initializes the binary tree object

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.root = None
		self.numNodes = 0


	def __str__(self):
		""" Returns string representation of tree object

		Returns:
			String representation of tree object

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in tree
			Space Complexity: O(N)

		"""

		if not self.root:
			return str([])

		Q = [self.root]
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



	def insert(self, val):
		""" Inserts a new node with value val

		Args:
			val: Value at noe

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in the tree
			Space Complexity: O(1)

		"""

		if not self.root:
			self.root = BinaryTreeNode(val)

		else:
			Q = [self.root]
			while Q:
				node = Q.pop(0)
				if not node.left:
					node.left = BinaryTreeNode(val)
					break
				else:
					Q.append(node.left)

				if not node.right:
					node.right = BinaryTreeNode(val)
					break
				else:
					Q.append(node.right)

		self.numNodes += 1


	def find(self, val):
		""" Finds if a node with value val exists in the tree

		Args:
			val: Value at the node

		Returns:
			True if a node with value val exists in the tree

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in the tree
			Space Complexity: O(1)

		"""

		if not self.root:
			return None

		Q = [self.root]
		while Q:
			node = Q.pop(0)

			if node.val == val:
				return node

			if node.left:
				Q.append(node.left)

			if node.right:
				Q.append(node.right)

		return None


	def getRandomNode(self):
		""" Returns a random node from the tree

		Returns:
			A random node from the tree

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes
			Space Complexity: O(1)

		"""

		if not self.root:
			return None

		import random

		index = random.randint(0, self.numNodes - 1)
		i = 0
		Q = [self.root]

		while Q:
			node = Q.pop(0)

			if i == index:
				return node

			if node.left:
				Q.append(node.left)

			if node.right:
				Q.append(node.right)

			i += 1

		return None


	def delete(self, val):
		""" Deletes a node with value val in the tree if it exists

		Args:
			val: Value at node

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in tree
			Space Complexity: O(1)

		"""

		self.root = self.deleteHelper(self.root, val)
		self.numNodes = 0
		if self.root:
			Q = [self.root]
			while Q:
				node = Q.pop(0)
				if node.left:
					Q.append(node.left)
				if node.right:
					Q.append(node.right)
				self.numNodes += 1


	def deleteHelper(self, root, val):
		""" Helper to delete function

		Args:
			root: Root node of the tree
			val: Value to be deleted

		Returns:
			Root node after deletion (if deletion is possible)

		Complexity Analysis:
			Time Complexity: O(N), N = number of nodes in tree
			Space Complexity: O(1)

		""" 

		if not root:
			return None

		currNumNodes = self.numNodes
		if root.val == val:
			self.numNodes -= 1
			if root.left:
				root.val = root.left.val 
				root.left = self.deleteHelper(root.left, root.left.val)
			elif root.right:
				root.val = root.right.val
				root.right = self.deleteHelper(root.right, root.right.val)
			else:
				root = None

		if self.numNodes == currNumNodes:
			root.left = self.deleteHelper(root.left, val)

		if self.numNodes == currNumNodes:
			root.right = self.deleteHelper(root.right, val)

		return root






# TESTING
Tree = BinaryTree()
print(Tree.getRandomNode())
print(Tree.delete(1))
print(Tree)
print(Tree.find(1))

Tree.insert(1)
print(Tree, Tree.numNodes)
Tree.insert(2)
print(Tree, Tree.numNodes)
Tree.insert(3)
print(Tree, Tree.numNodes)
Tree.delete(3)
print(Tree, Tree.numNodes)
Tree.delete(2)
print(Tree, Tree.numNodes)
Tree.delete(1)
print(Tree, Tree.numNodes)

Tree.insert(1)
Tree.insert(2)
Tree.insert(3)
Tree.insert(1)
Tree.insert(2)
Tree.insert(3)
Tree.insert(1)
print(Tree, Tree.numNodes)
Tree.delete(2)
print(Tree, Tree.numNodes)
Tree.delete(3)
print(Tree, Tree.numNodes)































