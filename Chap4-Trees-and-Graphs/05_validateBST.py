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




def validateBST(root):
	""" Validates if binary tree is a binary search tree

	Args:
		root: Root of binary tree

	Returns:
		True if binary tree is a binary search tree, False otherwise

	Assumptions:
		Empty tree is a valid BST

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in binary tree
		Space Complexity: O(N)

	"""

	inOrd = inOrderTraversal(root)

	for i in range(1, len(inOrd)):
		if inOrd[i] < inOrd[i-1]:
			return False

	return True




def inOrderTraversal(root):
	""" Returns a list of inorder traversal of given tree

	Args:
		root: Root node of the tree

	Returns:
		Inorder traversal as a list

	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in binary tree
		Space Complexity: O(N)

	"""

	if not root:
		return []

	return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)





print(validateBST(None))

T = BinaryTreeNode(1)
print(validateBST(T))

T.left = BinaryTreeNode(2)
print(validateBST(T))

T.val = 5
print(validateBST(T))

T.right = BinaryTreeNode(4)
print(validateBST(T))

T.right.val = 8
T.right.left = BinaryTreeNode(6)
print(validateBST(T))

T.right.right = BinaryTreeNode(9)
T.right.right.right = BinaryTreeNode(10)
print(validateBST(T))






















