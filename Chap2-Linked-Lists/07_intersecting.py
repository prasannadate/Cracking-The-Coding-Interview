def intersecting(L1, L2):
	""" Checks if two linked lists are intersecting (by reference), i.e. they share
		a node at the same memory address

	Args:
		L1: First linked list
		L2: Second linked list

	Returns:
		True if linked lists are intersecting, False otherwise

	Assumptions:
		1. L1 and L2 are LinkedList objects
		2. L1 and L2 have pointers to their respective head nodes
		3. Empty linked lists are not intersecting

	"""

	nodes = set()
	curr = L1.head

	while curr:
		nodes.add(curr)
		curr = curr.next

	curr = L2.head
	while curr:
		if curr in nodes:
			return True
		curr = curr.next

	return False




# TESTING
from linked_list import LinkedList 

L1 = LinkedList()
L2 = LinkedList()

L1.add(1)
L1.add(5)
L1.add(3)

L2.add(2)
L2.add(4)
L2.add(6)
L2.head.next.next = L1.head.next.next

print(L1)
print(L2)
print(intersecting(L1, L2))