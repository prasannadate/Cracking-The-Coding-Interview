def isUnique(string):
	""" Uses the inbuilt data structure set() in Python.

	Args:
		string: Input 

	Returns:
		boolean: True or False

	Assumptions:
		Empty string is unique string.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)
	
	"""

	return len(string) == len(set(string))



def isUnique2(string):
	""" Without using additional data structures - Part 2 of the question
	
	Args:
		string: Input string

	Returns:
		boolean: True or False

	Assumptions:
		Empty string is unique string.

	Complexity Analysis:
		Time Complexity: O(N^2)
		Space Complexity: O(N)
	"""

	for i in range(len(string)):
		for j in range(i+1, len(string)):
			if string[i] == string[j]:
				return False
	return True




# TESTING
strings = ["", "a", "ab", "aa", "abcdefg", "abcdefga"]

for string in strings:
	print(string)
	print("isUnique():", isUnique(string))
	print("isUnique2():", isUnique2(string))
	print("")