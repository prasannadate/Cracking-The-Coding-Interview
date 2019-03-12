def recursiveMultiply(a, b):
	""" Multiplies a and b

	Args:
		a: First positive integer
		b: Second positive integer

	Returns:
		Product of a and b, i.e. a * b

	Complexity Analysis:
		Time Complexity: O(min(log(a), log(b)))
		Space Complexity: O(min(log(a), log(b)))

	"""

	if a == 0 or b == 0:
		return 0

	if b % 2:
		return a + recursiveMultiply(a << 1, b >> 1)
	else:
		return recursiveMultiply(a << 1, b >> 1)




# TESTING
print(recursiveMultiply(0,0))
print(recursiveMultiply(1,0))
print(recursiveMultiply(0,1))
print(recursiveMultiply(1,1))
print(recursiveMultiply(2,1))
print(recursiveMultiply(3,2))
print(recursiveMultiply(3,1))
print(recursiveMultiply(6,4))
print(recursiveMultiply(5,7))






















