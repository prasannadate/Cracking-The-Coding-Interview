class ThreeStack:
	""" Implementing three stacks using a single array

	Args:
		stackSize: Size of each of the three stacks
		stacks: List containing all three stacks
		last: Indices of last elements of stack

	Methods:
		push(stackID, val): Pushes val onto stack stackID
		pop(stackID): Pops stack with stackID
		peek(stackID): Returns topmost element of stack with stackID
		isEmpty(stackID): Returns True if stack stackID is empty
		isFull(stackID): Returns True if stack stackID is full
		isInvalid(stackID): Returns True is stackID is invalid

	"""

	def __init__(self, stackSize):
		""" Initializes the stack

		Args:
			stackSize: Size of each of the three stacks

		Assumptions:
			stackSize is an integer

		Complexity Analysis:
			Time Complexity: O(stackSize)
			Space Complexity: O(stackSize)

		"""

		self.stackSize = stackSize
		self.stacks = [None] * stackSize * 3
		self.last = [None] * 3


	def __str__(self):
		return str(self.stacks)


	def push(self, stackID, val):
		""" Appends new value to end of stack with stackID

		Args:
			stackID: ID of the stack where push is to be performed
			val: Value to be pushed

		Raises:
			ValueError: If stackID is invalid

		Assumptions:
			1. stackID is integer
			2. val is integer

		Complexity Analysis:
			Time Complexity: O(stackSize) ammortized, O(1) usually
			Space Complexity: O(stackSize) ammortized, O(1) usually

		"""

		if self.isInvalid(stackID):
			raise ValueError("Invalid stack ID " + str(stackID))
		if self.isEmpty(stackID):
			self.last[stackID] = stackID * self.stackSize
		elif self.isFull(stackID):
			self.stacks = self.stacks[:self.stackSize] + \
							[None] * self.stackSize + \
							self.stacks[self.stackSize : self.stackSize * 2] + \
							[None] * self.stackSize + \
							self.stacks[self.stackSize * 2 :] + \
							[None] * self.stackSize
			for i, l in enumerate(self.last):
				self.last[i] = i * self.stackSize + l
			self.last[stackID] += 1
			self.stackSize *= 2
		else:
			self.last[stackID] += 1
		self.stacks[self.last[stackID]] = val


	def pop(self, stackID):
		""" Pops the last element of stack stackID and returns it

		Args:
			stackID: ID of the stack where pop is to be performed
		
		Returns:
			val: The popped value

		Raises:
			ValueError: If stackID is invalid, if stack is empty

		Assumptions:
			stackID is integer

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isInvalid(stackID):
			raise ValueError("Invalid stack ID " + str(stackID))
		if self.isEmpty(stackID):
			raise ValueError("Stack " + str(stackID) + " is empty")
		val = self.stacks[self.last[stackID]]
		self.stacks[self.last[stackID]] = None
		if self.last[stackID] == stackID * self.stackSize:
			self.last[stackID] = None
		else:
			self.last[stackID] -= 1
		return val


	def peek(self, stackID):
		""" Returns the value stored at the top of the stack with stackID

		Args:
			stackID: ID of the stack where pop is to be performed

		Returns:
			Value stored at top of the stack with stackID

		Raises:
			ValueError: If stackID is invalid, if stack is empty

		Assumptions:
			stackID is integer

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isInvalid(stackID):
			raise ValueError("Invalid stack ID " + str(stackID))
		if self.isEmpty(stackID):
			raise ValueError("Stack " + str(stackID) + " is empty")
		return self.stacks[self.last[stackID]]


	def isEmpty(self, stackID):
		""" Returns True if stack with stackID is empty

		Args:
			stackID: ID of the stack to be checked

		Returns:
			True if stack with stackID is empty

		Raises:
			ValueError: If stackID is invalid

		Assumptions:
			stackID is integer

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isInvalid(stackID):
			raise ValueError("Invalid stack ID " + str(stackID))
		if self.last[stackID] is None:
			return True
		else:
			return False


	def isFull(self, stackID):
		""" Returns True if stack with stackID is full

		Args:
			stackID: ID of the stack to be checked

		Returns:
			True if stack with stackID is full

		Raises:
			ValueError: If stackID is invalid

		Assumptions:
			stackID is integer

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isInvalid(stackID):
			raise ValueError("Invalid stack ID " + str(stackID))
		if self.last[stackID] == (stackID + 1) * self.stackSize - 1:
			return True
		else:
			return False


	def isInvalid(self, stackID):
		""" Returns True if stack with stackID is invalid

		Args:
			stackID: ID of the stack to be checked

		Returns:
			True if stackID is invalid

		Assumptions:
			stackID is integer

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if stackID < 0 or stackID >= len(self.last):
			return True
		else:
			return False





# TESTNG
S = ThreeStack(2)
print(S.isEmpty(0), S.isEmpty(1), S.isEmpty(2))
print(S.isFull(0), S.isFull(1), S.isFull(2))
S.push(0, 0)
S.push(1, 10)
S.push(2, 100)
print(S)
print(S.pop(0))
print(S.pop(1))
print(S.pop(2))
print(S)
S.push(0, 0)
S.push(0, 1)
S.push(1, 10)
S.push(1, 11)
S.push(2, 100)
S.push(2, 101)
print(S)
S.pop(0)
S.pop(1)
S.pop(2)
print(S)
S.push(0, 1)
S.push(0, 2)
print(S)
S.pop(2)
print(S)
S.push(2, 100)
S.push(2, 101)
S.push(0, 3)
S.push(0, 4)
print(S)
S.pop(1)
print(S)
S.pop(2)
print(S)


















