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


def checkSubtree(T1, T2):
	""" Checks if a subtree in T1 equals T2

	Args:
		T1: First tree node
		T2: Second tree node
	
	Returns:
		True if T2 is a subtree of T1

	Assumptions:
		T1 and T2 are objects of BinaryTreeNode class

	Complexity Analysis:
		Time Complexity: O(N1), N1 is number of nodes in T1
		Space Complexity: O(1)

	"""

	if not T1 and not T2:
		return True

	if not T1 or not T2:
		return False

	Q = [T1]

	while Q:
		T = Q.pop(0)
		if T.val == T2.val:
			if isEqual(T, T2):
				return True

		if T.left:
			Q.append(T.left)

		if T.right:
			Q.append(T.right)

	return False




def isEqual(T1, T2):
	""" Checks if two trees T1 and T2 are equal

	Args:
		T1: First tree node
		T2: Second tree node

	Assumptions:
		T1 and T2 are objects of BinaryTreeNode class

	Complexity Analysis:
		Time Complexity: O(N1), N1 is the number of nodes in T1
		Space Complexity: O(1)

	"""
	if not T1 and not T2:
		return True

	if not T1 or not T2:
		return False

	if T1.val == T2.val:
		return isEqual(T1.left, T2.left) and isEqual(T1.right, T2.right)

	return False






# TESTING
T1 = None
T2 = None
print(checkSubtree(T1, T2))

T1 = BinaryTreeNode(1)
T2 = BinaryTreeNode(2)
print(checkSubtree(T1, T2))

T1 = BinaryTreeNode(1)
T1.left = BinaryTreeNode(2)
T1.right = BinaryTreeNode(3)
T1.left.left = BinaryTreeNode(4)
T1.left.right = BinaryTreeNode(5)
T1.left.left.left = BinaryTreeNode(7)
T1.left.left.right = BinaryTreeNode(2)
T1.left.right = BinaryTreeNode(5)
T1.left.right.left = BinaryTreeNode(8)
T1.left.right.right = BinaryTreeNode(7)
T1.right.right = BinaryTreeNode(3)
T1.right.left = BinaryTreeNode(6)
T1.right.right = BinaryTreeNode(6)
T1.right.left.left = BinaryTreeNode(5)
T1.right.left.right = BinaryTreeNode(1)
T1.right.right = BinaryTreeNode(6)
T1.right.right.left = BinaryTreeNode(1)
T1.right.right.right = BinaryTreeNode(3)

T2 = BinaryTreeNode(6)

print(checkSubtree(T1, T2))

T2.left = BinaryTreeNode(1)
T2.right = BinaryTreeNode(3)
print(checkSubtree(T1, T2))

