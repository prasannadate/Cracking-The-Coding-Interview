def powerSet(A):
	""" Returns the power set of the set A

	Args:
		A: Input list

	Returns:
		Power set of A

	Complexity Analysis:
		Time Complexity: O(2^n), n = length of A
		Space Complexity: O(2^n)

	"""

	if not A:
		return [[]]

	power = powerSet(A[1:])

	for p in power[:]:
		power.append(p + [A[0]])
	return power




# TESTING
print(powerSet([]))
print(powerSet([1]))
print(powerSet([1,2]))
print(powerSet([1,2,3]))
print(powerSet([1,2,3,4]))
print(powerSet([1,2,3,4,5]))