class LinkedListNode:
	""" Linked list node

	Args:
		val: Value at node
		next: Pointer to next node

	"""

	def __init__(self, val):
		""" Initializes the linked list node

		Args:
			val: Value at node

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.val = val
		self.next = None




class LinkedList:
	""" Linked list 

	Args:
		head: Head node of linked list
		tail: Tail node of linked list

	Methods:
		add(val): Adds node with value val to the linked list

	"""

	def __init__(self):
		""" Initializes the linked list
		
		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.head = None
		self.tail = None


	def __str__(self):
		""" String representation of linked list

		Returns:
			String representation of linked list

		"""

		linkedList = []
		curr = self.head
		while curr:
			linkedList.append(curr.val)
			curr = curr.next
		return str(linkedList)


	def add(self, val):
		""" Adds a node with value val to the linked list

		Args:
			val: Value at new node

		Time Complexity: O(1)
		Space Complexity: O(1)

		"""

		node = LinkedListNode(val)
		if self.tail is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node


	def isEmpty(self):
		""" Checks if linked list is empty

		Returns:
			True if linked list is empty, False otherwise

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		return self.head is None




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




def listOfDepths(root):
	""" Creates a linked list of all the nodes at each depth of tree with root root

	Args:
		root: Root node of the tree

	Returns:
		A list of linked list, each linked list is a linked list of all nodes at 
		that level
	
	Complexity Analysis:
		Time Complexity: O(N), N = number of nodes in the tree
		Space Complexity: O(N)

	"""

	Q = [[root]]
	lists = []

	while Q:
		nodes = Q.pop(0)
		currLevel = LinkedList()
		nextLevel = []

		while nodes:
			n = nodes.pop(0)
			currLevel.add(n.val)

			if n.left:
				nextLevel.append(n.left)

			if n.right:
				nextLevel.append(n.right)

		if not currLevel.isEmpty():
			lists.append(currLevel)

		if nextLevel:
			Q.append(nextLevel)

	return lists




T = BinaryTreeNode(1)
T.left = BinaryTreeNode(2)
T.right = BinaryTreeNode(3)
T.left.left = BinaryTreeNode(4)
T.left.right = BinaryTreeNode(5)
T.right.left = BinaryTreeNode(6)
T.right.right = BinaryTreeNode(7)

levelLists = listOfDepths(T)
levelLists = [str(L) for L in levelLists]
print(levelLists)






















