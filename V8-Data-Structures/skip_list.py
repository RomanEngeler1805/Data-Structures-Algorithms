import numpy as np
import random

class Node(object):
	'''
	class to create node for linked list
	'''
	def __init__(self, key, level):
		self.key = key
		self.forward = [None]* (level+1) # high-way level

class SkipList(object):
	'''
	class to create and manage linked list
	'''
	def __init__(self, max_level, frac):
		self.MAX_LEVEL = max_level
		self.frac = frac # the step ratio between subsequent levels
		self.header = self.createNode(-1, self.MAX_LEVEL) # create header with key -1

		self.level = 0

	def randomLevel(self):
		# generate random level for new inserted node
		level = 0
		while random.random() < self.frac and level < self.MAX_LEVEL:
			level +=1
		return level

	def createNode(self, key, level):
		return Node(key, level)

	def insertNode(self, key):
		# insert node into linked list
		update = self.searchNode(key) # list of postdecessor
		current = update[0].forward[0] # position of current key

		if current == None or current.key != key: # check if key already in list
			# generate random level
			rlevel = self.randomLevel()

			# if we initialize a new level, link to header
			if rlevel > self.level:
				for i in range(self.level+ 1, rlevel+ 1):
					update[i] = self.header
				self.level = rlevel

			n = self.createNode(key, rlevel)
			
			# link node to postdecessors
			for i in range(rlevel+1):
				n.forward[i] = update[i].forward[i]
				update[i].forward[i] = n 
		
	def deleteNode():
		# to be implemented
		pass

	def searchNode(self, key):
		# find position of key
		update = [None]* (self.MAX_LEVEL+ 1)
		current = self.header

		# traverse list levels remembering the next larger element
		for i in range(self.level, -1, -1):
			while current.forward[i] and current.forward[i].key < key:
				current = current.forward[i]
			update[i] = current

		return update


	def printList(self):
		# function to print different levels of list
		head = self.header
		for lvl in range(self.level+1):
			print("Level {}: ".format(lvl), end=" ")
			node = head.forward[lvl]
			while(node != None):
				print(node.key, end=" ")
				node = node.forward[lvl]
			print(" ")


if __name__ == "__main__":
	sklist = SkipList(10, 0.5)
	for i in range(10):
		print(i)
		sklist.insertNode(np.random.randint(99))

	sklist.printList()
