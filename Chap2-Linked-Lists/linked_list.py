class LinkedListNode:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None




class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0


	def __str__(self):
		vals = []
		curr = self.head
		while curr:
			vals.append(curr.val)
			curr = curr.next
		return str(vals)


	def add(self, val):
		node = LinkedListNode(val)
		if not self.head or not self.tail:
			self.head = node
			self.tail = node
			self.length += 1
		else:
			node.prev = self.tail
			self.tail.next = node
			self.tail = self.tail.next
			self.length += 1


	def delete(self, val):
		if not self.head or not self.tail:
			return None
		if self.head == self.tail and self.head.val == val:
			self.head = None
			self.tail = None
			self.length -= 1
		elif self.head.val == val:
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
		elif self.tail.val == val:
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1
		else:
			curr = self.head
			while curr:
				if curr.val == val:
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					self.length -= 1
					break
				curr = curr.next


	def addAt(self, index, val):
		node = LinkedListNode(val)
		if not self.head or not self.tail:
			if index == 0:
				self.head = node
				self.tail = node
				self.length += 1
		elif self.head and self.tail and index == 0:
			node.next = self.head
			self.head.prev = node
			self.head = node
			self.length += 1
		elif index == self.length:
			self.tail.next = node
			node.prev = self.tail
			self.tail = self.tail.next
			self.length += 1
		else:
			curr = self.head
			i = 0
			while curr:
				if i == index:
					curr.prev.next = node
					node.prev = curr.prev
					node.next = curr
					curr.prev = node
					self.length += 1
					break
				curr = curr.next
				i += 1
			

	def deleteAt(self, index):
		if not self.head or not self.tail:
			return None
		if self.head == self.tail and index == 0:
			self.head = None
			self.tail = None
			self.length -= 1
		elif index == 0:
			self.head = self.head.next
			self.head.prev = None
			self.length -= 1
		elif index == self.length - 1:
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1
		else:
			i = 0
			curr = self.head
			while curr:
				if i == index:
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					self.length -= 1
					break
				curr = curr.next
				i += 1


	def find(self, val):
		i = 0
		curr = self.head
		while curr:
			if curr.val == val:
				return i
			curr = curr.next
			i += 1
		return -1


	def reverseOrder(self):
		vals = []
		curr = self.tail
		while curr:
			vals.append(curr.val)
			curr = curr.prev
		return vals


	def reverse(self):
		curr = self.head
		while curr:
			curr.next, curr.prev = curr.prev, curr.next
			curr = curr.prev
		self.head, self.tail = self.tail, self.head






# TESTING
# LL = LinkedList()
# LL.delete(0)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.add(0)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.delete(0)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.add(0)
# LL.add(1)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.delete(0)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.add(2)
# LL.add(3)
# LL.add(4)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.delete(4)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.delete(2)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.delete(1)
# LL.delete(3)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# print("")


# LL.deleteAt(0)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# print(LL.find(0))
# LL.addAt(1, 1)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.addAt(0, 1)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# print(LL.find(1))
# LL.deleteAt(0)
# print(LL, LL.head, LL.tail, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.addAt(0, 0)
# LL.addAt(1, 1)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.deleteAt(0)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.addAt(1, 1)
# LL.addAt(2, 3)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.deleteAt(1)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# LL.addAt(2, 2)
# print(LL, LL.head.val, LL.tail.val, LL.length)
# print("Reverse Order:", LL.reverseOrder())
# print(LL.find(4))
# print(LL.find(3))
# print(LL.find(1))






