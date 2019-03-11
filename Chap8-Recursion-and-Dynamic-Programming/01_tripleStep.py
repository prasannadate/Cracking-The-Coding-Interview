def tripleStep(n):
	""" Counts the number of ways to climb n steps when at each time, one can climb
			either one or two or three steps

	Args:
		n: Number of steps

	Returns:
		Number of ways to climb n steps as per above rule

	Complexity Analysis:
		Time Complexity: O(n)
		Space Complexity: O(n)

	"""

	return tripleStepHelper(n, [0]*n)




def tripleStepHelper(n, memo):
	""" Helper to tripleStep(n) function

	Args:
		n: Number of steps
		memo: Memoization array

	Returns:
		Number of ways of climbing n steps

	Complexity Analysis:
		Time Complexity: O(n)
		Space Complexity: O(n)

	"""

	if n == 0:
		return 0

	if memo[n-1] != 0:
		return memo[n-1]

	if n == 1:
		memo[n-1] = 1
		return 1
	if n == 2:
		memo[n-1] = 2
		return 2
	if n == 3:
		memo[n-1] = 4
		return 4

	memo[n-1] = tripleStepHelper(n-1, memo) + tripleStepHelper(n-2, memo) + \
				tripleStepHelper(n-3, memo)

	return memo[n-1]




def tripleStepFast(n):
	""" Counts the number of ways to climb n steps when at each time, one can climb
			either one or two or three steps

	Args:
		n: Number of steps

	Returns:
		Number of ways to climb n steps as per above rule

	Complexity Analysis:
		Time Complexity: O(n)
		Space Complexity: O(1)

	"""

	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4

	a, b, c = 1, 2, 4

	for i in range(3, n):
		a, b, c = b, c, a + b + c

	return c




# TESTING
for i in range(31):
	print(i, tripleStep(i), tripleStepFast(i))


































