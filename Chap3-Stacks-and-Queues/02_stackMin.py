class StackMin:
	""" A stack which keeps track of the minimum element

	Args:
		data: Data values stored in the stack
		minimum: Minimum values of the stack

	Methods:
		push(val): Pushes val into the stack
		pop(): Pops the last element of the stack
		peek(): Returns value at the last element of stack
		getMin(): Returns the minimum value of the stack
		isEmpty(): Returns True if stack is empty

	"""

	def __init__(self):
		""" Initializes the stack
		
		"""

		self.data = []
		self.min = []


	def __str__(self):
		return str(self.data)


	def push(self, val):
		""" Pushes val into the stack

		Args:
			val: Value to be pushed into the stack

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			self.data.append(val)
			self.min.append(val)

		else:
			if val < self.min[-1]:
				self.min.append(val)
			else:
				self.min.append(self.min[-1])
			self.data.append(val)


	def pop(self):
		""" Pops the last element of the stack

		Returns:
			Value at the last element of the stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Stack is empty")

		self.min.pop()
		return self.data.pop()


	def peek(self):
		""" Returns value at the last element of the stack

		Returns:
			Value at the last element of the stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Stack is empty")

		return self.data[-1]


	def getMin(self):
		""" Returns the minimum value in the stack
		
		Returns:
			Minimum value in the stack

		Raises:
			ValueError: If stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Stack is empty")

		return self.min[-1]


	def isEmpty(self):
		""" Checks if stack is empty

		Returns:
			True if stack is empty

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if not self.data:
			return True
		else:
			return False





# TESTING
S = StackMin()
print(S.isEmpty())
S.push(5)
print(S)
print(S.getMin())
S.push(3)
print(S)
print(S.getMin())
print(S.pop())
print(S)
print(S.getMin())
S.push(2)
S.push(4)
print(S)
print(S.getMin())
print(S.pop())
print(S)
print(S.getMin())
S.push(7)
S.push(4)
S.push(2)
S.push(4)
print(S)
print(S.getMin())
print(S.pop())
print(S.pop())
print(S)
print(S.getMin())
S.push(1)
S.push(1)
S.push(4)
print(S)
print(S.getMin())






















