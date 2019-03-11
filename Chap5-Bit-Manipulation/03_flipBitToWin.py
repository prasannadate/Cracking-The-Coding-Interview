def flipBitToWin(A):
	""" Finds length of longest sequence of 1s after flipping exactly 1 zero in the
			binary representation of A

	Args:
		A: 32 bit integer

	Returns:
		Length of longest sequence of 1s after flipping exactly 1 zero in the binary
			representation of A

	Complexity Analysis:
		Time Complexity: O(N), N = log(A) is the number of bits in binary 
			representation of A
		Space Complexity: O(1)

	"""

	if A == 0:
		return 1

	B = '0' + bin(A)[2:] + '0'

	longest = 0
	start = None
	intermediateZero = False

	for i in range(1, len(B) - 1):
		if B[i] == '1':
			if start is None:
				start = i

		elif intermediateZero:
			if i - start > longest:
				longest = i - start
			if B[i-1] == '1':
				start = i
				while B[start - 1] == '1':
					start -= 1
			else:
				start = None
				intermediateZero = False

		else:
			if B[i+1] == '1':
				intermediateZero = True
				if start is None:
					start = i
			else:
				if start is not None and i - start + 1 > longest:
					longest = i - start + 1
				start = None

	if start and len(B) - 1 - start > longest:
		longest = len(B) - 1 - start

	return longest



for i in range(127):
	print(i, bin(i)[2:], flipBitToWin(i))