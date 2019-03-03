def stringRotation(str1, str2):
	""" Returns True if str2 is a rotation of str1.

	Args:
		str1: First input string (control string)
		str2: Second input string (experimental string)

	Returns:
		True if str2 is a rotation of str1

	Assumption:
		Empty string is a rotation of empty string

	Complexity Analysis:
		Time Complexity: O(1) because isSubstring() is considered as blackbox - 
		the function has already been given to us.
		Space Complexity: O(1)

	"""

	if len(str1) == len(str2):
		return isSubstring(str1 + str1, str2)
	else:
		return False



def isSubstring(str1, str2):
	""" Returns True if str2 is a substring of str1.

	Args:
		str1: First input string
		str2: Second input string

	Returns:
		True if str2 is a substring of str1

	Assumptions:
		Empty string is a substring of everything

	Complexity Analysis:
		Time Complexity: O(M*N), where M is length of str1 and N is length of str2
		Space Complexity: O(1)

	"""

	return str2 in str1




# TESTING
strings = [["", ""], ["", "a"], ["ab", "ba"], ["abc", "bac"], \
	["erbottlewat", "waterbottle"]]

for str1, str2 in strings:
	print("String1:", str1)
	print("String2:", str2)
	print(stringRotation(str1, str2))
	print("")







