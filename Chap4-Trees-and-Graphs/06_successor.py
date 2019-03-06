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



def leftMost(node):
	""" Returns the leftmost node in the right subtree of node in an inorder sequence

	Args:
		node: Current node

	Returns:
		Leftmost node in the right subtree as in an inorder traversal sequence

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""
	
	if not node:
		return None

	if node.left:
		return leftMost(node.left)

	else:
		return node




def parentHelper(node):
	""" Finds the next node in an inorder traversal when node is a right leaf

	Args:
		node: Current node

	Returns:
		Next node in an inorder traversal when node is a right leaf

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	if not node:
		return None

	parent = node.parent

	if not parent:
		return None

	elif node == parent.left:
		return parent

	else:
		return parentHelper(parent)





def successor(node):
	""" Returns the successor of node in an inorder traversal setting

	Args:
		node: Current node

	Returns: 
		Next node in an inorder traversal setting

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	if not node:
		return None

	if not node.left and not node.right:
		if node.parent:
			if node == node.parent.left:
				return node.parent
			else:
				return parentHelper(node)

	else:
		return leftMost(node.right)





a = BinaryTreeNode(6)
b = BinaryTreeNode(2)
c = BinaryTreeNode(8)
d = BinaryTreeNode(1)
e = BinaryTreeNode(4)
f = BinaryTreeNode(7)
g = BinaryTreeNode(9)
h = BinaryTreeNode(3)
i = BinaryTreeNode(5)
j = BinaryTreeNode(10)
k = BinaryTreeNode(11)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
e.left = h
e.right = i
i.right = j
j.right = k

print(setParent(a))
print(a.parent, b.parent.val, c.parent.val, d.parent.val, e.parent.val, \
	f.parent.val, g.parent.val, h.parent.val, i.parent.val, j.parent.val, k.parent.val)

print(successor(a).val)
print(successor(b).val)
print(successor(c).val)
print(successor(d).val)
print(successor(e).val)
print(successor(f).val)
print(successor(g))
print(successor(h).val)
print(successor(i).val)
print(successor(j).val)
print(successor(k).val)



























