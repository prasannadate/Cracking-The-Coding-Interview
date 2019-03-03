def returnKthToLast(LL, K):
	""" Returns Kth from the last element

	Args:
		LL: Linked list object
		K: Integer

	Returns:
		Value stored at Kth from the last element

	Assumptions:
		Linked list object has pointer to head element of the linked list

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(1)
	"""

	curr = LL.head
	N = 0
	while curr:
		N += 1
		curr = curr.next

	i = 0
	curr = LL.head
	while curr:
		if i == N - K:
			return curr.val 
		curr = curr.next
		i += 1

	return None



# TESTING
from linked_list import LinkedList 

LL = LinkedList()
LL.add(0)
LL.add(1)
LL.add(2)
LL.add(3)
LL.add(4)
LL.add(5)

print(LL)
print(returnKthToLast(LL, 0))
print(returnKthToLast(LL, 1))
print(returnKthToLast(LL, 2))
print(returnKthToLast(LL, 3))
print(returnKthToLast(LL, 4))
print(returnKthToLast(LL, 5))
print(returnKthToLast(LL, 6))
print(returnKthToLast(LL, 7))