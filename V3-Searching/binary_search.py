import numpy as np

def BSearch(arr, l, r, b):
	m = int((r+l)/2)

	if l > r:
		return 0
	elif b == arr[m]:
		return m
	elif b < arr[m]:
		return(BSearch(arr, l, m-1,b))
	else:
		return BSearch(arr, m+1, r, b)	


if __name__ == "__main__":
	arr = np.array([2, 8, 1, 6, 3, 9])
	left = 0
	right = len(arr)
	b = 6

	sol = BSearch(arr, left, right, b)

	print('array: '+ str(arr))
	print('element '+ str(b)+ ' found at position '+ str(sol))
