def rotateMatrix(A):
	""" Rotates an NXN matrix 90 degrees clockwise in place.

	Args:
		A: Input matrix (list of lists)

	Returns:
		Rotated version of A
	
	Assumptions:
		A is a list of list

	Complexity Analysis:
		Time Complexity: O(N^2)
		Space Complexity: O(1)

	"""

	if not A:
		return None

	if len(A) != len(A[0]):
		return None

	N = len(A)

	for i in range(len(A) // 2):
		for j in range(i, N-i-1):
			A[i][j], A[N-j-1][i], A[N-i-1][N-j-1], A[j][N-i-1] = \
				A[N-j-1][i], A[N-i-1][N-j-1], A[j][N-i-1], A[i][j]

	return A



# TESTING
As = [[], [[]], [[1]], [[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]], \
	[[1,2,3,4,5],[6,7,8,9,0],[1,3,5,7,9],[2,4,6,8,0],[1,4,7,0,3]]]

for A in As:
	print(A)
	print(rotateMatrix(A))
	print("")