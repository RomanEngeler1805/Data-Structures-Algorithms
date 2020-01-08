import numpy as np
from copy import deepcopy

def BubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

	return arr

if __name__ == "__main__":
	arr = np.array([4, 8, 2, 9, 3, 7])

	arr_sorted = BubbleSort(deepcopy(arr))

	print('Unsorted array: '+ str(arr))
	print('Sorted array: '+ str(arr_sorted))
