def conversion(A, B):
	""" Determines number of bits that would need to be flipped to convert integer 
			A to B

	Args:
		A: 32 bit integer
		B: 32 bit integer

	Returns:
		Number of bits that would need to be flipped to convert A to be

	Complexity Analysis:
		Time Complexity: O(1)
		Space Complexity: O(1)

	"""

	return bin(A ^ B).count('1')




# TESTING
print(conversion(3, 0))
print(conversion(7, 3))
print(conversion(10,5))
