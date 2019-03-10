def insertion(N, M, i, j):
	""" Given two 32 bit numbers N and M, and two bit positions i and j, inserts
			M into N such that M starts at bit j and ends at bit i

	Args:
		N: 32 bit number 
		M: 32 bit number to be inserted
		i: Ending index from the least significant bit
		j: Starting index from the least significant bit

	Returns:
		Result of the above operation

	Assumptions:
		Bits i through j have enough space to fit all of M

	Complexity Analysis:
		Time Complexity: O(N), N = number of bits
		Space Complexity: O(1)

	"""

	mask = (-1 << (j+1)) | (~(-1 << i))
	return (N & mask) | (M << i)



# TESTING
N = 141
M = 9
print(bin(N))
print(bin(M))
res = insertion(N, M, 1, 4)
print(bin(res))

N = int("10000000000", 2)
M = int("10011", 2)
print(bin(N))
print(bin(M))
res = insertion(N, M, 2, 6)
print(bin(res))