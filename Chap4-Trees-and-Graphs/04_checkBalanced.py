class BinaryTreeNode:
	""" Binary tree node

	Args: 
		val: Value at node
		left: Left subtree of node
		right: Right subtree of node

	"""

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None




def checkBalanced(root):
	""" Checks if binary tree starting at root is balanced

	Args:
		root: Root of the binary tree

	Returns:
		True if binary tree is balanced, False otherwise

	Assumptions:
		Empty tree is not balanced

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in binary tree
		Space Complexity: O(N)

	"""

	if not root:
		return False

	leftHeight = heightOf(root.left)
	rightHeight = heightOf(root.right)

	if abs(leftHeight - rightHeight) > 1:
		return False
	else:
		return True



def heightOf(root):
	""" Computes the height of binary tree

	Args:
		root: Root node of the binary tree

	Returns:
		Height of the binary tree

	Assumptions:
		Empty tree has zero height

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in binary tree
		Space Complexity: O(N)

	"""

	if root is None:
		return 0

	leftHeight = heightOf(root.left)
	rightHeight = heightOf(root.right)

	return 1 + max(leftHeight, rightHeight)





print(checkBalanced(None))
T = BinaryTreeNode(1)
print(checkBalanced(T))

T.left = BinaryTreeNode(2)
print(checkBalanced(T))

T.left.left = BinaryTreeNode(3)
print(checkBalanced(T))

T.right = BinaryTreeNode(3)
T.left.left = BinaryTreeNode(4)
print(checkBalanced(T))

T.left.right = BinaryTreeNode(5)
T.right.left = BinaryTreeNode(6)
T.right.right = BinaryTreeNode(7)
print(checkBalanced(T))

T = BinaryTreeNode(1)
T.left = BinaryTreeNode(2)
T.right = BinaryTreeNode(3)
T.right.left = BinaryTreeNode(4)
T.right.left.right = BinaryTreeNode(5)
print(checkBalanced(T))

T.right.left.right = None
T.right.right = BinaryTreeNode(5)
print(checkBalanced(T))

T.right.right.right = BinaryTreeNode(6)
print(checkBalanced(T))







