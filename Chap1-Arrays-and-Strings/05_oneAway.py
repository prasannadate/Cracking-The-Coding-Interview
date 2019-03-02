def oneAway(str1, str2):
	""" Returns True if str1 and str2 are at most 1 edit away.
	
	1 edit is defined as inserting a character, deleting a character or replacing
	a character.

	Args:
		str1: First input string
		str2: Second input string

	Returns:
		True if input strings are at most one edit away, False otherwise.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(1)

	"""

	if len(str1) == len(str2):
		return oneReplace(str1, str2)
	else:
		return oneDelete(str1, str2)



def oneReplace(str1, str2):
	""" Returns True if str1 and str2 would be equal after replacing at most 1 
	character in either one of them.

	Args:
		str1: First input string
		str2: Second input string

	Returns:
		True if input strings differ by at most one character.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(1)

	"""

	count = 0
	for i in range(len(str1)):
		if str1[i] != str2[i]:
			count += 1
	return count <= 1




def oneDelete(str1, str2):
	""" Returns True if str1 would be equal to str2 after deleting at most one 
	character from either of the strings.

	Args:
		str1: First input string
		str2: Second input string

	Returns:
		True if input strings would be equal after deleting at most one character 
		from either one of the strings.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(1)

	"""

	if abs(len(str1) - len(str2)) != 1:
		return False

	count = 0
	i = 0
	j = 0

	while i < len(str1) and j < len(str2):
		if str1[i] != str2[j]:
			count += 1
			if len(str1) > len(str2):
				i += 1
			else:
				j += 1
		else:
			i += 1
			j += 1

	return count <= 1




# TEST

strings = [["", ""], ["", "a"], ["a", ""], ["", "ab"], ["ab", "ba"], ["ab", "ac"], \
			["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]]

for str1, str2 in strings:
	print("String 1:", str1)
	print("String 2:", str2)
	print(oneAway(str1, str2))
	print("")




