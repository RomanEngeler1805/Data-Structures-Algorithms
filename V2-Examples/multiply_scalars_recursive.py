import numpy as np
import sys

def f(a,b):
	if (b == 1):
		return a
	elif (b%2 == 0):
		return f(2*a, b/2)
	else:
		return a+ f(2*a, (b-1)/2)

if __name__ == "__main__":
	print('Number 1: '+ sys.argv[1])
	print('Number 2: '+ sys.argv[2])
	print('Product: '+ str(f(int(sys.argv[1]),

					int(sys.argv[2]))))
