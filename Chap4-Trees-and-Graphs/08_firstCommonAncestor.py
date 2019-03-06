class BinaryTreeNode:
	""" Binary tree node

	Args: 
		val: Value at node
		left: Left subtree of node
		right: Right subtree of node
		parent: Parent of node

	"""

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None




def setParent(root):
	""" Sets parent nodes for all tree nodes beginning at root

	Args:
		root: Root node of the tree

	Returns:
		Tree root node with all the parent pointers set properly

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in the tree
		Space Complexity: O(1)

	"""

	Q = [root]
	tree = []

	while Q:
		node = Q.pop(0)
		tree.append(node.val)

		if node.left:
			node.left.parent = node
			Q.append(node.left)

		if node.right:
			node.right.parent = node
			Q.append(node.right)

	return tree





def firstCommonAncestor(a, b):
	""" Finds the first common ancestor of a and b

	Args:
		a: First node of the tree
		b: Second node of the tree

	Returns:
		First common ancestor node

	Complexity Analysis:
		Time Complexity: O(log(N)), N = number of nodes in the tree
		Space Complexity: O(log(N))

	"""

	parenta = findAncestors(a)
	parentb = findAncestors(b)

	i = len(parenta) - 1
	j = len(parentb) - 1

	while i >= 0 and j >= 0 and parenta[i] == parentb[j]:
		i -= 1
		j -= 1

	return parenta[i+1]



def findAncestors(node):
	""" Finds all ancestors of node in the tree

	Args:
		node: Node of the tree

	Returns:
		A list of all the ancestors

	Complexity Analysis:
		Time Complexity: O(log(N)), N = number of nodes in the tree
		Space Complexity: O(log(N))

	"""

	parents = []
	curr = node
	while curr:
		parents.append(curr.parent)
		curr = curr.parent

	return parents








a = BinaryTreeNode(1)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3)
d = BinaryTreeNode(4)
e = BinaryTreeNode(5)
f = BinaryTreeNode(6)
g = BinaryTreeNode(7)
h = BinaryTreeNode(8)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = h
e.left = f
e.right = g

print(setParent(a))

print(firstCommonAncestor(a,b))
print(firstCommonAncestor(b,c).val)
print(firstCommonAncestor(b,h).val)
print(firstCommonAncestor(c,d).val)
print(firstCommonAncestor(d,f).val)
print(firstCommonAncestor(d,g).val)
print(firstCommonAncestor(d,e).val)
print(firstCommonAncestor(f,g).val)










































