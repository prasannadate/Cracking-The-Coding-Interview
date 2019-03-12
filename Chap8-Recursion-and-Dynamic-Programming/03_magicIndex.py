def magicIndex(A):
	""" An index i is a magic index if A[i] = i. This function finds a magic index 
			in A if it exists.

	Args:
		A: Sorted array of integers

	Returns:
		Magic index if it exists, -1 otherwise

	Complexity Analysis:
		Time Complexity: O(log(N)), N = length of A
		Space Complexity: O(1)

	"""

	if not A:
		return -1

	low = 0
	high = len(A) - 1

	while low <= high:
		mid = (low + high) // 2

		if A[mid] == mid:
			return mid

		elif A[mid] > mid:
			high = mid - 1

		else:
			low = mid + 1

	return -1




# TESTING
A = []
print(magicIndex(A))

A = [2]
print(magicIndex(A))

A = [-1]
print(magicIndex(A))

A = [0]
print(magicIndex(A))

A = [-1, 0, 1, 2, 3, 4, 6]
print(magicIndex(A))

A = [-1, 0, 1, 4, 4, 5]
print(magicIndex(A))

A = [0, 2, 4, 6]
print(magicIndex(A))

A = [0, 2, 4, 6, 8]
print(magicIndex(A))

A = [0, 1, 2, 3, 4, 5]
print(magicIndex(A))

A = [1, 2]
print(magicIndex(A))

A = [-1, 1]
print(magicIndex(A))