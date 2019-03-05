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
		length: Length of the stack

	Methods:
		push(val): Pushes val onto stack
		pop(): Pops value from the stack
		peek(): Returns value at the top of the stack
		getLength(): Returns the length of stack
		isEmpty(): Checks if stack is empty

	"""

	def __init__(self):
		""" Initializes the stack

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.head = None
		self.length = 0


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
		self.length += 1


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
		self.length -= 1
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


	def getLength(self):
		""" Returns the length of the stack

		Returns:
			Length of the stack

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		return self.length


	def isEmpty(self):
		""" Checks if stack is empty

		Returns:
			True if stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Conmplexity: O(1)

		"""

		return self.head is None










class SuperStack:
	""" Stack of stacks, each stack within this has some finite capacity

	Args:
		head: Head of the super stack
		capacity: Capacity of each stack within super stack

	Methods:
		push(val): Pushes a value into super stack
		pop(): Pops the topmost value from super stack
		peek(): Peeks at the topmost value in super stack
		isEmpty(): Checks if super stack is empty

	"""

	def __init__(self, capacity):
		""" Initializes the super stack

		Args:
			capacity: Capacity of the super stack
		
		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		self.head = []
		self.capacity = capacity


	def __str__(self):
		""" Returns string representation of super stack

		Returns:
			String representation of super stack

		Complexity Analysis:
			Time Complexity: O(N), N = number of elements in super stack
			Space Complexity: O(N)

		"""

		if self.isEmpty():
			return "[]"

		superStack = "["
		for i in range(len(self.head) - 1, -1, -1):
			superStack += ' ' + self.head[i].__str__() + ','
		return superStack[:-1] + " ]"


	def push(self, val):
		""" Pushes a value into super stack

		Args:
			val: Value to be pushed

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty() or self.head[-1].length >= self.capacity:
			stack = Stack()
			stack.push(val)
			self.head.append(stack)
		else:
			self.head[-1].push(val)


	def pop(self):
		""" Pops topmost value from super stack

		Returns:
			Topmost value from super stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Super stack is empty")

		val = self.head[-1].pop()
		if self.head[-1].length == 0:
			self.head.pop()
		return val


	def peek(self):
		""" Peeks at the super stack

		Returns: 
			Topmost value in the super stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Super stack is full")

		return self.head[-1].peek()


	def isEmpty(self):
		""" Checks if super stack is empty
		
		Returns:
			True if super stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		return self.head == []






# TESTING
S = SuperStack(2)
print(S)
print(S.isEmpty())
S.push(9)
print(S)
print(S.pop())
print(S)
S.push(3)
S.push(4)
print(S)
print(S.pop())
print(S)
S.push(2)
S.push(7)
print(S)
print(S.pop())
print(S)
S.push(5)
S.push(1)
S.push(8)
S.push(6)
S.push(2)
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())
print(S)
print(S.pop())


















































