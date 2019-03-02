def palindromePermutation(string):
	""" Checks if given string is a permutation of a palindrome.

	Args:
		string: Input string.

	Returns:
		boolean: True or False

	Assumptions:
		1. Don't care about spaces, e.g. "tact coa" should return True because it
		is a permutation of "taco cat", which is a palindrome (excluding spaces).
		2. Don't care about case, e.g. "Taco Cat" should return True because it is
		a permutation of "taco cat", which is a palindrom (excluding case).
		3. Empty string return True

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	string = ''.join(string.split(' ')).lower()
	sig = getSignature(string)
	count = 0
	for c in sig:
		if sig[c] % 2 == 1:
			if count:
				return False
			else:
				count += 1
	return True




def getSignature(string):
	""" Returns the signature of a string.

	Signature of a string is defined as tabulaitng the number of occurrances of
	every character in the string.

	Args:
		string: String

	Returns:
		Dictionary with keys as characters in the string, and values as their
		counts.

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
strings = ["", "a", "ab", "aba", "abab", "AbaB", "Aba", "aBA", "Tact Coa", "a b c"]

for string in strings:
	print(string)
	print(palindromePermutation(string))
	print("")


















