def pairwiseSwap(A):
	""" Swaps odd and even bits of A

	Args:
		A: 32 bit integer

	Returns:
		Number with odd and even bits of A swapped

	Assumptions:
		A is a 32 bit integer

	Complexity Analysis:
		Time Complexity: O(1)
		Space Complexity: O(1)

	"""

	maskOdd = int("AAAAAAAA", 16)
	maskEven = int("55555555", 16)
	return ((A & maskEven) << 1) ^ ((A & maskOdd) >> 1)




# TESTING
print(bin(10))
print(bin(pairwiseSwap(10)))

print(bin(13))
print(bin(pairwiseSwap(13)))