import numpy as np
from copy import deepcopy

def SiftDown(arr, i, m):
	while 2*i < m: # XXX
		j = 2*i
		if j< m and arr[j] < arr[j+1]:
			j+= 1
		if arr[i] < arr[j]:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i = j
		else:
			i = m

	return arr

def HeapSort(arr, n):
	for i in range(int(n/2)-1, 0, -1):
		arr = SiftDown(arr, i, n)
	for i in range(n-1, 0,-1):
		temp = arr[0]
		arr[0] = arr[i]
		arr[i] = temp
		arr = SiftDown(arr, 0, i-1)

	return arr

if __name__ == "__main__":
	#arr = np.array([7, 6, 4, 5, 1, 2])
	arr = np.array([7, 2, 5, 4, 3, 6, 1])
	#arr = np.array([2, 6, 3, 1, 4, 5])
	
	arr_sorted = HeapSort(deepcopy(arr), len(arr))

	print('Unsorted array: '+ str(arr))
	print('Sorted array: '+ str(arr_sorted))
