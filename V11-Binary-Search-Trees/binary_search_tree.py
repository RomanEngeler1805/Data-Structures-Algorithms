import numpy as np

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key

def insert(root, node):
	''' insert new node '''
	if not root:
		root = node
	else:
		if root.key < node.key:
			# need to define pointer to node (e.g. root.right = node)
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		elif root.key > node.key:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

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
		return

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
	r = Node(50)
	for i in range(10, 80, 10):
		insert(r, Node(i))

	print('complete tree:')
	inorder(r)

	print('leaf removed:')
	remove(r, 40)
	inorder(r)

	print('Minimum element:')
	find_min(r)
