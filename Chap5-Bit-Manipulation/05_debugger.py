def debugger(n):
	""" Checks if n is a power of 2

	Args:
		n: 32 bit integer

	Returns:
		True if n is a power of 2, False otherwise

	Complexity Analysis:
		Time Complexity: O(1)
		Space Complexity: O(1)

	"""

	return (n & (n-1)) == 0



print(2, debugger(2))
print(3, debugger(3))
print(4, debugger(4))
print(6, debugger(6))
print(16, debugger(16))