def zeroMatrix(A):
	""" Sets ith row and jth column to zero if A[i][j] equals 0

	Args:
		A: Input matrix

	Returns:
		Matrix with zeroed out ith row and jth column if A[i][j] equals 0

	Assumptions:
		A has to be 2 dimensional matrix

	Complexity Analysis:
		Time Complexity: O(M*N), where M is number of rows and N is number of 
		columns in matrix A
		Space Complexity: O(M+N), where M is number of rows and N is number of 
		columns in matrix A

	"""

	if not A:
		return None

	if not A[0]:
		return None

	rows = set()
	cols = set()

	for i in range(len(A)):
		for j in range(len(A[0])):
			if A[i][j] == 0:
				rows.add(i)
				cols.add(j)

	for i in range(len(A)):
		for j in range(len(A[0])):
			if i in rows or j in cols:
				A[i][j] = 0

	return A



# TESTING
As = [[], [[]], [[1]], [[0]], [[0,1],[1,0]], [[1,2],[3,4]], [[1,2,0],[2,3,0], \
		[0,4,5]], [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,0],[0,4,7,8,9],[2,0,4,0,5]]]

for A in As:
	print(A)
	print(zeroMatrix(A))
	print("")