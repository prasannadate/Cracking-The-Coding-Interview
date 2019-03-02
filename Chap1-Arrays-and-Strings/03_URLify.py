def URLify(string):
	""" Replaces all spaces in a string with '%20'.

	Args:
		string: Input string

	Assumption:
		Empty string shoud be returned as it is.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	return "%20".join(string.split(' '))



# TESTING
strings = ["", "a", "ab", "a b", "abc", "a b c", "Mr. John Smith", "a  b  c"]
for string in strings:
	print(string)
	print(URLify(string))
	print("")