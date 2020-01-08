import numpy as np
from copy import deepcopy
import time

def find_minimum(arr):
	min_value = np.inf
	min_idx = 0

	for i in range(len(arr)):
		if arr[i] < min_value:
			min_idx = i
			min_value = arr[i] 
	
	return min_idx

def find_element(arr, k):
	for i in range(k-1):
		idx = find_minimum(arr)
		arr.pop(idx)
	
	idx = find_minimum(arr)

	return arr[idx]

if __name__ == "__main__":
	arr = [2, 7, 8, 4, 2, 7, 9]
	k = 3

	t_start = time.time()
	val = find_element(deepcopy(arr), k)
	duration = round((time.time()- t_start)* 1e3, 5)
	print('Time complexity: '+ str(duration)+ ' ms')

	print(arr)
	print(str(k)+ '-th smallest element is '+ str(val))
