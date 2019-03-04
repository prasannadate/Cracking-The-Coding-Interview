class AnimalShelter:
	""" Animal shelter sheltering dogs and cats

	Args:
		animals: Queue of all animals in the shelter
		numDogs: Number of dogs in the shelter
		numCats: Number of cats in the shelter

	Methods:
		enqueue(animal): Enqueue animal into the shelter
		dequeueAny(): Dequeues the oldest animal in the shelter
		dequeueDog(): Dequeues the oldest dog in the shelter
		dequeueCat(): Dequeues the oldest cat in the shelter
		isEmpty(): Checks if animal shelter is empty

	"""

	def __init__(self):
		""" Initializes the animal shelter
		
		"""

		self.animals = []
		self.numDogs = 0
		self.numCats = 0


	def __str__(self):
		return str(self.animals)


	def enqueue(self, animal):
		""" Enqueues new animal into the shelter

		Args:
			animal: Animal to be enqueued

		Raises:
			ValueError: If animal is invalid

		Assumptions:
			animal is "dog" or "cat"

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if animal != "dog" and animal != "cat":
			raise ValueError("Cannot admit " + animal + ", can only admit 'dog'" + \
				" and 'cat'")

		self.animals.append(animal)
		if animal == "dog":
			self.numDogs += 1
		if animal == "cat":
			self.numCats += 1


	def dequeueAny(self):
		""" Dequeues the oldest (based on arrival time) animal from shelter

		Returns:
			Oldest animal from shelter

		Raises:
			ValueError: If animal is invalid

		Complexity Analysis:
			Time Complexity: O(1)
			Space Complexity: O(1)

		"""

		if self.isEmpty():
			raise ValueError("Animal shelter is empty")

		if self.animals[0] == "dog":
			self.numDogs -= 1

		if self.animals[0] == "cat":
			self.numCats -= 1

		return self.animals.pop(0)


	def dequeueDog(self):
		""" Dequeues the oldest dog from the shelter

		Returns:
			Oldest dog from shelter

		Raises:
			ValueError: If there are no dogs in the shelter

		Complexity Analysis:
			Time Complexity: O(N)
			Space Complexity: O(1)

		"""

		if self.numDogs <= 0:
			raise ValueError("Insufficient dogs in the animal shelter")

		self.numDogs -= 1
		for i, animal in enumerate(self.animals):
			if animal == "dog":
				return self.animals.pop(i)


	def dequeueCat(self):
		""" Dequeues the oldest cat from the shelter

		Returns:
			Oldest cat from shelter

		Raises:
			ValueError: If there are no cats in the shelter

		Complexity Analysis:
			Time Complexity: O(N)
			Space Complexity: O(1)

		"""

		if self.numCats <= 0:
			raise ValueError("Insufficient cats in the animal shelter")

		self.numCats -= 1
		for i, animal in enumerate(self.animals):
			if animal == "cat":
				return self.animals.pop(i)


	def isEmpty(self):
		""" Checks if animal shelter is empty

		"""

		if not self.animals:
			return True
		else:
			return False






# TESTING
S = AnimalShelter()
print(S.isEmpty())
S.enqueue("dog")
print(S)
print(S.dequeueDog())
print(S)
S.enqueue("dog")
S.enqueue("dog")
S.enqueue("cat")
S.enqueue("dog")
print(S)
print(S.dequeueCat())
print(S)
print(S.dequeueDog())
print(S.dequeueDog())
print(S.dequeueDog())
print(S)
S.enqueue("cat")
S.enqueue("cat")
S.enqueue("cat")
S.enqueue("dog")
print(S)
print(S.dequeueDog())
print(S)
S.enqueue("dog")
S.enqueue("cat")
S.enqueue("dog")
S.enqueue("dog")
S.enqueue("cat")
print(S)
print(S.dequeueDog())
print(S)






























