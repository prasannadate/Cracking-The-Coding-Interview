class StackNode:
	""" Linked list node for stack

	Args:
		val: Value stored at the node
		next: Pointer to the next node in the stack

	"""

	def __init__(self, val):
		""" Initializes the node

		Args:
			val: Value to be stored at the node
			next: Pointer to next node

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.val = val
		self.next = None




class Stack:
	""" Linked list as stack

	Args:
		head: Pointer to the head of the stack

	Methods:
		push(val): Pushes val onto stack
		pop(): Pops value from the stack
		peek(): Returns value at the top of the stack
		isEmpty(): Checks if stack is empty

	"""

	def __init__(self):
		""" Initializes the stack

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.head = None


	def __str__(self):
		""" Returns string representation of stack

		Returns:
			String representation of stack

		Complexity Analysis:
			Time Complexity: O(N)
			Space Complexity: O(N)

		"""

		stack = []
		curr = self.head
		while curr:
			stack.append(curr.val)
			curr = curr.next
		return str(stack)


	def push(self, val):
		""" Pushes val onto the stack

		Args:
			val: Value to be pushed

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		node = StackNode(val)
		node.next = self.head
		self.head = node


	def pop(self):
		""" Pops top of the stack

		Returns:
			Value in the node at the top of stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Stack is empty")

		node = self.head
		self.head = self.head.next
		return node.val


	def peek(self):
		""" Peeks at the topmost node

		Returns:
			Value in the topmost node

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Stack is empty")

		return self.head.val


	def isEmpty(self):
		""" Checks if stack is empty

		Returns:
			True if stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Conmplexity: O(1)

		"""

		return self.head is None




def sortStack(S):
	""" Returns a sorted version of input stack S

	Args:
		S: Stack object

	Returns:
		Sorted stack

	Assumptions:
		S is an object of Stack class defined above

	Complexity Analysis:
		Time Complexity: O(N^2), N = number of elements in S
		Space Complexity: O(N)

	"""

	T = Stack()

	# Get length of input stack S
	lenS = 0
	curr = S.head
	while curr:
		lenS += 1
		curr = curr.next

	# Populate output stack T
	previous = float("inf")
	greatest = -float("inf")
	count = 0

	while lenS > 0:
		greatest = -float("inf")
		count = 0
		curr = S.head

		while curr:
			if curr.val > greatest and curr.val < previous:
				greatest = curr.val
				count = 1

			elif curr.val == greatest:
				count += 1

			curr = curr.next

		lenS -= count

		while count > 0:
			 T.push(greatest)
			 count -= 1

		previous = greatest

	return T




# TESTING
S = Stack()
S.push(4)
S.push(2)
S.push(8)
S.push(5)
S.push(1)
print(S)
print(S.pop())
print(S)
print(S.peek())
print(sortStack(S))































