import numpy as np
from copy import deepcopy

def BinarySearch(arr, l, r, b):
	m = int((r+l)/2)

	if l > r:
		return l
	elif b == arr[m]:
		return m
	elif b < arr[m]:
		return BinarySearch(arr, l, m-1,b)
	else:
		return BinarySearch(arr, m+1, r, b)

def InsertionSort(arr):
	for i in range(1, len(arr)):
		x = arr[i]
		p = BinarySearch(arr, 0, i-1, x)

		#print(x)
		#print(p)

		for j in range(i-1, p-1, -1):
			arr[j+1] = arr[j]
		arr[p] = x

	return arr

if __name__ == "__main__":
	arr = np.array([4, 8, -5, 2, 12, 9, 3, 7])

	arr_sorted = InsertionSort(deepcopy(arr))

	print('Unsorted array: '+ str(arr))
	print('Sorted array: '+ str(arr_sorted))
