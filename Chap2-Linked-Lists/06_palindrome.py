def palindrome(L):
	""" Checks if a linked list is a palindrome

	Args:
		L: LinkedList object

	Returns:
		True if L is a palindrome, False otherwise

	Assumptions:
		1. L is a LinkedList object
		2. L has pointer to head of the linked list
		3. Empty list is a palindrome

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	vals = []
	curr = L.head

	while curr:
		vals.append(curr.val)
		curr = curr.next

	i = 0
	j = len(vals) - 1

	while i < j:
		if vals[i] != vals[j]:
			return False
		i += 1
		j -= 1

	return True




# TESTING
from linked_list import LinkedList 

L = LinkedList()
L.add("m")
L.add("a")
L.add("l")
L.add("a")
L.add("y")
L.add("a")
L.add("l")
L.add("a")
L.add("m")

print(L)
print(palindrome(L))