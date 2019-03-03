def loopDetection(L):
	""" Checks if a loop exists in the linked list. If it exists, returns the 
		starting node of the loop.

	Args:
		L: LinkedList object

	Returns:
		Starting node of the loop if loop exists, None otherwise.

	Assumption:
		1. L is a LinkedList object
		2. L has a pointer to head node of the linked list
		3. Empty linked lists do not have loops

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	nodes = set()
	curr = L.head

	while curr:
		if curr in nodes:
			return curr
		else:
			nodes.add(curr)
		curr = curr.next

	return None



# TESTING
from linked_list import LinkedList 

L = LinkedList()
L.add(1)
L.add(2)
L.add(5)
L.add(10)
L.add(4)

print(L)
print(loopDetection(L))

L.tail.next = L.head.next.next
print(loopDetection(L).val)