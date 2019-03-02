def stringCompression(string):
	""" Returns compressed version of string if it is shorter, else returns 
	original string.
	
	Args:
		string: Input string

	Returns:
		Compressed version of string if it is shorter, else returns original string.
		For example, compressed version of "aabbbcc" would be "a2b3c2", and in this 
		case, the compressed version would be returned because it is shorter. 
		On the other hand compressed version of "abcd" is "a1b1c1d1", and in this
		case, original will be returned because compressed version is longer.

	Assumptions:
		Input string contains only lower case letters.

	Complexity Analysis:
		Time Complexity: O(N)
		Space Complexity: O(N)

	"""

	if not string:
		return string

	chars = [string[0]]
	count = [1]

	for i in range(1, len(string)):
		if string[i] == chars[-1]:
			count[-1] += 1

		else:
			chars.append(string[i])
			count.append(1)

	comp = ''.join([chars[i] + str(count[i]) for i in range(len(chars))])

	if len(comp) < len(string):
		return comp
	else:
		return string





# TESTING
strings = ["", "a", "aa", "aaa", "aabb", "aabbcc", "aaabb", "aaabbb", "aaabbbccc", \
			"aabcccccaaa", "aabbccdddccc"]

for string in strings:
	print(string)
	print(stringCompression(string))
	print("")
