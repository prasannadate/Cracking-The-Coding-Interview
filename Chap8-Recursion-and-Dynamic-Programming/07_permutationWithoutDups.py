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




def permutation(A):
	""" Given a list of elements, returns all possible permutations that can be 
			formed from those numbers. 

	Args:
		A: List of elements

	Returns:
		A list of all possible permutations

	Assumptions:
		A does not contain duplicate elements

	Complexity Analysis:
		Time Complexity: O(N!), N = length of A
		Space Complexity: O(N!)

	"""

	if not A:
		return [[]]

	if len(A) == 1:
		return [A]

	perms = permutation(A[1:])
	ans = []

	for i in range(len(perms[:])):
		for j in range(len(perms[i])):
			ans.append(perms[i][0:j] + [A[0]] + perms[i][j:])
		ans.append(perms[i] + [A[0]])

	return ans






# TESTING
# A = [5,4,3,2,1]
# for i in range(120):
# 	A = permute(A)
# 	print(A)



A = ['a', 'b', 'c']
print(permutation(A))


































