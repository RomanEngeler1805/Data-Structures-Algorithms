import numpy as np
import sys

def f(a,b):
	res = 0
	while (b > 0):
		if (b%2 != 0):
			res += a
		a *= 2
		b = int(b / 2)
	return res

if __name__ == "__main__":
	print('Number 1: '+ sys.argv[1])
	print('Number 2: '+ sys.argv[2])
	print('Product: '+ str(f(int(sys.argv[1]),
				int(sys.argv[2]))))
