import numpy as np

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		self.height = 1

def insert(root, key):
	''' insert new node
	needs to return a node for the pointer s.t.
	tree can be climbed bottom up '''
	# insert node as usual
	if root is None:
		return Node(key)
	elif root.key < key:
		root.right = insert(root.right, key)
	else:
		root.left = insert(root.left, key)
	
	# update height of parent
	root.height = 1+ max(getHeight(root.left),
				getHeight(root.right))

	# balance factor
	balance = getBalance(root)
	
	# different cases if unbalanced
	# left left
	if balance > 1 and key < root.left.key:
		return rightRotate(root)
		
	# righ right
	if balance < -1 and key > root.right.key:
		return leftRotate(root)
	
	
	# left right
	if balance > 1 and key > root.left.key:
		root.left = leftRotate(root.left)
		return rightRotate(root)

	# right left
	if balance < -1 and key < root.right.key:
		root.right = rightRotate(root.right)
		return leftRotate(root)
	
	return root
	

def leftRotate(z):
	y = z.right
	T2 = y.left
	
	# perform rotation
	y.left = z
	z.right = T2

	# update heights
	z.height = 1+ max(getHeight(z.left), getHeight(z.right))
	y.height = 1+ max(getHeight(y.left), getHeight(y.right))

	# return new root (necessary?)
	return y

def rightRotate(z):
	y = z.left
	T3 = y.right

	# perform rotation
	y.right = z
	z.left = T3

	# update heights
	z.height = 1+ max(getHeight(z.left), getHeight(z.right))
	y.height = 1+ max(getHeight(y.left), getHeight(y.right))

	# return new root
	return y

def getHeight(root):
	if not root:
		return 0

	return root.height

def getBalance(root):
	if not root:
		return 0
	
	return getHeight(root.left)- getHeight(root.right)

def search(root, key):
	''' search for key '''
	v = root
	while root is not None:
		if key == v.key:
			return v
		elif key < v.key:
			v = v.left
		else:
			v = v.right
	return None

def SymmetricSuccessor(root):
	''' find symmetric successor '''
	w = root.right
	x = root.left

	while x is not None:
		w = x
		x = x.left

	return w

def remove(root, key):
	''' remove key '''
	if root is None:
		return root

	# traverse until key is located
	if root.key < key:
		root.right = remove(root.right, key)
	elif root.key > key:
		root.left = remove(root.left, key)
	else:
		# no children
		if root.left is None and root.right is None:
			temp = None
			root = None
			return temp

		# one child (left)
		if root.right is None:
			temp = root.left
			root = None
			return temp

		# one child (right)
		if root.left is None:
			temp = root.right
			root = None
			return temp
		
		# two children
		temp = SymmetricSuccessor(root)
		root.key = temp.key
		root.right = remove(root.right, temp.key)

	# check if necessary
	if root is None:
		return root

	# update height of ancestors
	root.height = 1+ max(getHeight(root.left), getHeight(root.right))

	# get balance factor
	balance = getBalance(root)

	# check cases for unbalanced node
	# left left
	if balance > 1 and getBalance(root.left) >= 0:
		return rightRotate(root)
		
	# right right
	if balance < -1 and getBalance(root.right) <= 0:
		return leftRotate(root)
	
	# left right
	if balance > 1 and getBalance(root.left) < 0:
		root.left = leftRotate(root.left)
		return rightRotate(root)
	
	# right left
	if balance < -1 and getBalance(root.right) > 0:
		root.right = rightRotate(root.right)
		return leftRotate(root)

	return root

def find_min(root):
	''' find minimum key '''
	v = root
	while v.left:
		v = v.left

	print(v.key)
		
			

def inorder(root):
	if root:
		inorder(root.left)
		print(root.key)
		inorder(root.right)

def preorder(root):
	if root:
		print(root.key)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		pprint(root.key)

if __name__ == "__main__":
	root = None
	keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]

	for key in keys:
		root = insert(root, key)

	print('complete tree:')
	preorder(root)

	print('leaf removed:')
	root = remove(root, 10)
	preorder(root)

	print('Minimum element:')
	#find_min(r)
