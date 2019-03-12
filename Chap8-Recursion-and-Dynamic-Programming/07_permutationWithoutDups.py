def permute(A):
	""" Given a list A, returns the next permutation of A

	Args:
		A: Given permutation

	Returns:
		Next permutation of A, i.e. next largest number from all numbers in A

	Complexity Analysis:
		Time Complexity: O(N), N = number of elements in A
		Space Complexity: O(1)

	"""

	if not A:
		return []

	i = len(A) - 1
	while i > 0 and A[i-1] > A[i]:
		i -= 1

	if i == 0:
		return A[::-1]

	j = indexOfSmallestElementGreaterThan(A[i-1], A[i:])

	A = A[:i-1] + [A[i+j]] + A[:i+j:-1] + [A[i-1]] + A[i+j-1:i-1:-1]

	return A




def indexOfSmallestElementGreaterThan(val, B):
	""" Find index of smallest element in B that is greater than val

	Args:
		val: Value
		B: List 

	Returns:
		Index of smallest element in B that is greater than val

	Assumptions:
		B is sorted in reverse decreasing order

	Complexity Analysis:
		Time Complexity: O(N), N = length of B
		Space Complexity: O(N)

	"""

	i = 0
	while i < len(B):
		if B[i] < val:
			return i-1
		i += 1

	if B[i-1] > val:
		return i-1
	else:
		return -1




# TESTING
A = [5,4,3,2,1]
for i in range(120):
	A = permute(A)
	print(A)


































