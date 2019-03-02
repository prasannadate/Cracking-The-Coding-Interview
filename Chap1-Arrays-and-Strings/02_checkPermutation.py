def checkPermutation(str1, str2):
	""" Checks if str1 is a permutation of str2 and vice versa.

	Args:
		str1: String
		str2: String

	Assumption:
		Empty strings are permutations of each other.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	sig1 = getSignature(str1)
	sig2 = getSignature(str2)

	if len(sig1) != len(sig2):
		return False

	for c in sig1:
		if c not in sig2 or sig1[c] != sig2[c]:
			return False

	return True




def getSignature(string):
	""" Returns the signature of a string.

	Signature of a string is defined as tabulaitng the number of occurrances of
	every character in the string.

	Args:
		string: String

	Assumption:
		Signature of empty string is an empty dictionary.

	Complexity Analytis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	sig = {}
	for s in string:
		if s in sig:
			sig[s] += 1
		else:
			sig[s] = 1
	return sig




# TESTING
strings = [["", ""], ["", "a"], ["a", "a"], ["ab", "ab"], ["abc", "cba"], ["abd", "bcd"], ["abccd", "abcee"], ["abacbdd", "dabacbd"]]
for str1, str2 in strings:
	print("String1:", str1)
	print("String2:", str2)
	print(checkPermutation(str1, str2))
	print("")
	















