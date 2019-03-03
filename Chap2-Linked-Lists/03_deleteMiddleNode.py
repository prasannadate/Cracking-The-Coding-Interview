def deleteMiddleNode(LL, node):
	""" Deletes middle node (i.e. a node that is not head or tail) of a linked list

	Args:
		LL: Linked list object
		node: Linked list node object

	Returns:
		Does not return anything

	Assumptions:
		1. LL is a LinkedList object
		2. LL contains pointer to head node of the linked list
		3. node is a LinkedListNode object

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(1)

	"""

	if LL.head == node:
		LL.head = LL.head.next

	else:
		curr = LL.head
		prev = None
		while curr:
			if curr == node:
				prev.next = curr.next
				break
			prev = curr
			curr = curr.next



# TESTING
from linked_list import LinkedList 

LL = LinkedList()
LL.add(0)
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)

node = LL.head.next.next

print(LL)
deleteMiddleNode(LL, node)
print(LL)