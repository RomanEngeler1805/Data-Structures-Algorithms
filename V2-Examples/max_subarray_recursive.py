import time
import numpy as np
import sys

def suffix(arr):
	max_summ = 0
	start = len(arr)
	
	for i in range(len(arr), 0, -1):
		summ = np.sum(arr[i-1:])
		if summ > max_summ:
			max_summ = summ
			start = i-1 # to include zeroth element

	return max_summ

def prefix(arr):
	max_summ = 0
	end = 0
	
	for i in range(1, len(arr)+1): # to include last element
		summ = np.sum(arr[:i])
		if summ > max_summ:
			max_summ = summ
			end = i 

	return max_summ	

def max_subarr(arr):
	max_summ = 0
	start = 0
	end = 1

	if len(arr) <= 1:
		return np.max([arr, 0])
	else:
		split = int(len(arr)/ 2)
		arr1 = arr[:split]
		arr2 = arr[split:]

		W1 = max_subarr(arr1)
		W2 = max_subarr(arr2)
		W3 = suffix(arr1)+ prefix(arr2)	

	return np.max([W1, W2, W3])

if __name__ == "__main__":
	sample_arr = np.array([3, 8, -2, 5, -7, 4])

	if len(sys.argv) > 1:
		arr = []
		for num in range(1,len(sys.argv)):
			arr.append(int(sys.argv[num]))
		arr = np.asarray(arr)
		summ = max_subarr(arr)
	else:
		summ = max_subarr(sample_arr)

	print('Max sum: '+ str(summ))
