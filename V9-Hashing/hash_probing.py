import numpy as np

class hashing():
	def __init__(self, length):
		self.length = length
		self.count = 0
		self.max_probing = 5
		self.hash_table = [None]* self.length

	def hash_function(self, key):
		''' hash funtion (implement own version) '''
		return hash(key) % self.length

	def grow_table(self):
		''' to be implemented: function to increase table size  '''
		pass
	
	def insert(self, value):
		''' insert element into hash table '''
		key = self.hash_function(value)
		entry = self.hash_table[key]

		# probing
		it = 0
		key_prob = key
		while entry is not None:
			# check if same element already exists
			if value == entry:
				return

			# exit if too many probing
			if it >= self.max_probing:
				return

			it += 1
			# linear
			key_prob = (key+ it)% self.length
			# quadratic
			# key_prob = key+ int(it/2)^2* (-1)^(it+1)
			entry = self.hash_table[key_prob]

		self.hash_table[key_prob] = value	
				
	def search(self, value):
		''' search for element in hash table '''
		key = self.hash_function(value)
		entry = self.hash_table[key]

		# probing
		it = 0
		key_prob = key
		while (entry is not value):
			if entry is None:
				return -1, None

			if it >= self.max_probing:
				return -1, None
				
			it += 1
			# linear
			key_prob = (key+ it)% self.length
			
			entry = self.hash_table[key_prob]

		return key_prob, entry

	def remove(self, value):
		''' remove element from hash table '''
		key = self.hash_function(value)
		entry = self.hash_table[key]

		# probing
		it = 0
		key_prob = key
		while (entry is not value):
			if entry is None:
				return

			if it >= self.max_probing:
				return			

			it += 1
			# linear
			key_prob = (key+ it)% self.length
			entry = self.hash_table[key_prob]

		self.hash_table[key_prob] = None

	def print_table(self):
		''' print hash table '''
		for key in range(self.length):
			print(self.hash_table[key])

if __name__ == "__main__":
	# fill hash table
	h = hashing(8)
	for i in range(6):
		h.insert(np.random.randint(99))
	h.insert(5)

	#
	print('hash table:')
	h.print_table()
	print('search value 5: '+ str(h.search(5)))
	print('remove element 5')
	h.remove(5)
	print('updated hash table:')
	h.print_table()
