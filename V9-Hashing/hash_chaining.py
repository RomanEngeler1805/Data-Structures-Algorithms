import numpy as np

class hashing():
	def __init__(self, length):
		self.length = length
		self.hash_table = [[] for i in range(self.length)]

	def hash_function(self, key):
		return hash(key) % self.length
	
	def insert(self, value):
		''' insert element into hash table '''
		key = self.hash_function(value)		
		key_list = self.hash_table[key]
		
		# if hash key does not already exist
		if len(key_list) == 0:
			key_list.append((key, value))
			return
		
		# check if hash key with same value exists
		is_duplicate = False
		for i, kv in enumerate(key_list):
			k, v = kv
			if v == value:
				is_duplicate = True
				break
	
		if not is_duplicate:
			key_list.append((key, value))
				
	def search(self, value):
		''' search for element in hash table '''
		key = self.hash_function(value)
		key_list = self.hash_table[key]

		for i, kv in enumerate(key_list):
			k, v = kv
			if v == value:
				return key, v

	def remove(self, value):
		''' remove element from hash table '''
		key = self.hash_function(value)
		key_list = self.hash_table[key]
	
		for i, kv in enumerate(key_list):
			k, v = kv
			if v == value:
				key_list.pop(i) # use pop to remove element with index
				return

	def print_table(self):
		''' print hash table '''
		for key in range(self.length):
			print(self.hash_table[key])

if __name__ == "__main__":
	# fill hash table
	h = hashing(5)
	for i in range(10):
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
