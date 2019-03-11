def drawLine(screen, width, x1, x2, y):
	""" Draws a horizontal line on a screen

	Args:
		screen: An array of bytes, where each byte represents 8 pixels on screen
		width: Width of the screen in bits
		x1: X-coordinate of the first point
		x2: X-coordinate of the second point
		y: Y-coordinate of both points

	Returns:
		screen with line drawn

	Assumptions:
		1. Each byte in screen is represented as two hexadecimal digits
		2. width is in bits
		3. x1, x2 and y are in bits

	Complexity Analysis:
		Time Complexity: O(x2 - x1)
		Space Complexity: O(1)

	"""

	startBit = y * width + x1
	startByte = startBit // 8
	startShift = startBit % 8
	endBit = y * width + x2
	endByte = endBit // 8
	endShift = endBit % 8

	if startByte == endByte:
		byte = '0' * startShift + '1' * (endShift - startShift + 1) + '0' * (7 - endShift)
		byte = hex(int(byte, 2))[2:]
		screen[startByte] = byte
		return screen

	else:
		if startShift < 4:
			screen[startByte] = hex(15 >> startShift)[2:] + 'f'
		else:
			screen[startByte] = '0' + hex(15 >> (startShift - 4))[2:]

		screen[endByte] = hex((255 << (7 - endShift)) % 256)[2:]

		for i in range(startByte + 1, endByte):
			screen[i] = "ff"

		return screen




def showScreen(screen, width):
	""" Prints the screen

	Args:
		screen: Array of bytes, where each byte represents 8 pixels on screen
		width: Width in bits

	Complexity Analysis:
		Time Complexity: O(N), N = length of screen
		Space Complexity: O(1)

	"""

	screen = ''.join(screen)
	width = width // 4
	hex2bin = { '0': "0000",
				'1': "0001",
				'2': "0010",
				'3': "0011",
				'4': "0100",
				'5': "0101",
				'6': "0110",
				'7': "0111",
				'8': "1000",
				'9': "1001",
				'a': "1010",
				'b': "1011",
				'c': "1100",
				'd': "1101",
				'e': "1110",
				'f': "1111"}

	for i in range(len(screen) // width):
		string = ""
		for j in range(width):
			string += hex2bin[screen[i * width + j]]
		print(string)




# TESTING
screen = ['00'] * 32
width = 32
showScreen(screen, width)
print("")

screen = drawLine(screen, width, 2, 29, 5)
print(screen)
showScreen(screen, width)
