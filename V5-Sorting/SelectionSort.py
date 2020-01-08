import numpy as np
from copy import deepcopy

def SelectionSort(arr):
	for i in range(len(arr)-1):
		p = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[p]:
				p = j

		arr[i], arr[p] = swap(arr[i], arr[p])

	return arr

def swap(a, b):
	temp = a
	a = b
	b = temp
	return a, b

if __name__ == "__main__":
	arr = np.array([4, 8, 2, 9, 3, 7])

	arr_sorted = SelectionSort(deepcopy(arr))

	print('Unsorted array: '+ str(arr))
	print('Sorted array: '+ str(arr_sorted))
