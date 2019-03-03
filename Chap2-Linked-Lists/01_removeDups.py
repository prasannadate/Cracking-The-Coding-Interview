from linked_list import LinkedList


def removeDups(LL):
	vals = set()
	curr = LL.head
	prev = None

	while curr:
		if curr.val in vals:
			prev.next = curr.next
			curr = curr.next
		else:
			vals.add(curr.val)
			prev = curr
			curr = curr.next

	return LL


def removeDupsWithoutBuffer(LL):
	current = LL.head
	runner = None
	previous = None

	while current:
		runner = current.next
		previous = current

		while runner:
			if runner.val == current.val:
				previous.next = runner.next
				runn = runn.next
			else:
				previous = runner
				runner = runner.next
		current = current.next

	return LL


# TESTING
LL = LinkedList()
LL.add(1)
LL.add(2)
LL.add(1)
LL.add(2)
LL.add(1)
LL.add(3)
LL.add(4)
LL.add(2)
LL.add(2)
LL.add(2)
LL.add(2)
LL.add(4)
LL.add(5)
print(LL)
LL1 = removeDups(LL)
LL2 = removeDupsWithoutBuffer(LL)
print(LL1)
print(LL2)