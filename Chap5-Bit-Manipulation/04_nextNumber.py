def nextNumber(A):
	""" Given a positive integer, returns the next smallest and the next largest number
			that have the same number of 1 bits in their binary representation

	Args:
		A: Positive integer

	Returns:
		A pair containing the next smallest and the next largest number that have
			the same number of 1 bits in their binary representation

	Complexity Analysis:
		Time Complexity: O(N), N = number of bits in the binary representatino of A
		Space Complexity: O(1)

	"""

	B = bin(A)
	foundZero = False
	i = 0

	while i < len(B) - 2:
		if foundZero and B[len(B) - 1 - i] == '1':
			break
		if not foundZero and B[len(B) - 1 - i] == '0':
			foundZero = True
		i += 1

	if i == len(B) - 2:
		smallest = -1
	else:
		smallest = A - (1 << (i-1))

	foundOne = False
	i = 0

	while i < len(B) - 2:
		if foundOne and B[len(B) - 1 - i] == '0':
			break
		if not foundOne and B[len(B) - 1 - i] == '1':
			foundOne = True
		i += 1

	largest = A + (1 << (i-1))

	return smallest, largest





# TESTING
print(1, nextNumber(1))
print(2, nextNumber(2))
print(3, nextNumber(3))
print(4, nextNumber(4))
print(5, nextNumber(5))
print(6, nextNumber(6))
print(7, nextNumber(7))
print(8, nextNumber(8))
print(9, nextNumber(9))
print(10, nextNumber(10))
print(11, nextNumber(11))
print(12, nextNumber(12))
print(13, nextNumber(13))
print(14, nextNumber(14))
print(15, nextNumber(15))
print(16, nextNumber(16))
print(17, nextNumber(17))
print(18, nextNumber(18))