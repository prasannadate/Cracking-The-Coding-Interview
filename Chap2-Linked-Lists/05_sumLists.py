from linked_list import LinkedList 


def sumLists(L1, L2):
	""" Returns a linked list which contains the sum of numbers represented in L1
		and L2. L1 and L2 contain digits of the number with least significant bit 
		as the head of the linked list. For example: 
		754 is represented as 4 -> 5 -> 7

	Args:
		L1: LinkedList object
		L2: LinkedList object

	Returns:
		LinkedList object containing sum of L1 and L2 as per above description.

	Assumptions:
		L1 and L2 are LinkedList objects

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	L = LinkedList()
	carry = 0
	summation = 0
	curr1 = L1.head
	curr2 = L2.head

	while curr1 and curr2:
		summation = curr1.val + curr2.val + carry
		carry = summation // 10
		L.add(summation % 10)
		curr1 = curr1.next
		curr2 = curr2.next

	while curr1:
		summation = curr1.val + carry
		carry = summation // 10
		L.add(summation % 10)
		curr1 = curr1.next

	while curr2:
		summation = curr2.val + carry
		carry = summation // 10
		L.add(summation % 10)
		curr2 = curr2.next

	return L




def sumListsForward(L1, L2):
	""" Returns a linked list which contains the sum of numbers represented in L1
		and L2. L1 and L2 contain digits of the number with most significant bit 
		as the head of the linked list. For example: 
		754 is represented as 7 -> 5 -> 4

	Args:
		L1: LinkedList object
		L2: LinkedList object

	Returns:
		LinkedList object containing sum of L1 and L2 as per above description.

	Assumptions:
		L1 and L2 are LinkedList objects

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	L1.reverse()
	L2.reverse()
	L = sumLists(L1, L2)
	L.reverse()
	L1.reverse()
	L2.reverse()
	return L




# TESTING
L1 = LinkedList()
L2 = LinkedList()

L1.add(7)
L1.add(1)
L1.add(6)

L2.add(5)
L2.add(9)
L2.add(2)
L2.add(9)
L2.add(9)

print(L1)
print(L2)

S1 = sumLists(L1, L2)
S2 = sumListsForward(L1, L2)

print(S1)
print(S2)