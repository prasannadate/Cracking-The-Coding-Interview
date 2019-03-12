def robotInAGrid(grid):
	""" Finds a path for a robot starting at upper left corner in a 2D grid and 
			terminating at lower right corner

	Args:
		grid: Grid describing which squares are available and which are blocked

	Returns:
		Above described path for the robot as a list. Each element of the list 
			contains the coordinates of the next square where the robot is supposed
			to go

	Complexity Analysis:
		Time Complexity: O(R * C), R = number of rows in grid, C = number of columns
			in grid
		Space Complexity: O(R * C)

	"""

	path = [[[] for i in range(len(grid[0]))] for i in range(len(grid))]
	return robotInAGridHelper(grid, path, (0, 0))




def robotInAGridHelper(grid, path, start):
	""" Helper to robotInAGrid(grid) function

	Args:
		grid: Grid describing which squares are available and which are blocked
		path: 2D array containing paths from every square in grid to end
		(i, j): Coordinates of current square
	
	Returns:
		Path for a robot starting at (i,j) in grid and ending at bottom right square

	Complexity Analysis:
		Time Complexity: O(R * C), R = number of rows in grid, C = number of columns
			in grid
		Space Complexity: O(R * C)

	"""

	if not grid or not grid[0]:
		return []

	i, j = start

	if path[i][j]:
		return path[i][j]

	R = len(grid)
	C = len(grid[0])

	if i == R - 1 and j == C - 1:
		path[i][j] = [(i,j)]
		return path[i][j]

	downPath = []
	rightPath = []

	if i + 1 < R and grid[i+1][j]:
		downPath = robotInAGridHelper(grid, path, (i+1, j))

	if j + 1 < C and grid[i][j+1]:
		rightPath = robotInAGridHelper(grid, path, (i, j+1))

	if not downPath and not rightPath:
		return []

	if not downPath:
		if rightPath[-1] == (R-1, C-1):
			path[i][j] = [(i,j)] + rightPath
			return path[i][j]
		else:
			return []

	if not rightPath:
		if downPath[-1] == (R-1, C-1):
			path[i][j] = [(i,j)] + downPath
			return path[i][j]
		else:
			return []

	if downPath[-1] == (R-1, C-1) and rightPath[-1] == (R-1, C-1):
		if len(downPath) <= len(rightPath):
			path[i][j] = [(i,j)] + downPath + path[i][j]
		else:
			path[i][j] = [(i,j)] + rightPath + path[i][j]
		return path[i][j]

	if downPath[-1] == (R-1, C-1):
		path[i][j] = [(i, j)] + downPath + path[i][j]
		return path[i][j]

	if rightPath[-1] == (R-1, C-1):
		path[i][j] = [(i, j)] + rightPath + path[i][j]

	return []




# TESTING
grid = [[1 for i in range(3)] for i in range(3)]
print(robotInAGrid(grid))

grid[1][1] = 0
print(robotInAGrid(grid))

grid[1][0] = 0
print(robotInAGrid(grid))

grid[1][2] = 0
print(robotInAGrid(grid))

grid = [[1 for i in range(8)] for i in range(6)]
grid[0][3] = 0
grid[1][2] = 0
grid[1][6] = 0
grid[2][5] = 0
grid[3][1] = 0
grid[3][7] = 0
grid[4][2] = 0
grid[4][4] = 0
grid[4][6] = 0
grid[5][3] = 0
print(grid)
print(robotInAGrid(grid))






































