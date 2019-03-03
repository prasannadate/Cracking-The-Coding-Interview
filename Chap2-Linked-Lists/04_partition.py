def partition(LL, value):
	""" Partitions a linked list around a value such that all values less than given
		value are to the left and all values greater than or equal to the given
		value are to the right

	Args:
		LL: LinkedList object
		value: Integer value

	Returns:
		Partitioned linked list object

	Assumptions:
		1. LL is a LinkedList object
		2. LL has a pointer to the head of the linked list

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	values = []
	curr = LL.head
	while curr:
		if curr.val < value:
			values.insert(0, curr.val)
		else:
			values.append(curr.val)
		curr = curr.next

	curr = LL.head
	for v in values:
		curr.val = v
		curr = curr.next

	return LL




# TESTING 
from linked_list import LinkedList

LL = LinkedList()
LL.add(3)
LL.add(5)
LL.add(8)
LL.add(5)
LL.add(10)
LL.add(2)
LL.add(1)

print(LL)
LL = partition(LL, 5)
print(LL)