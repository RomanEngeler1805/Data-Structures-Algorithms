import numpy as np
from copy import deepcopy
import time

def partition(arr, l, r, pivot):
	while l < r:
		while arr[l] < pivot:
			l+= 1
		while arr[r] > pivot:
			r-= 1
		
		arr[l], arr[r] = arr[r], arr[l]

		if arr[l] == arr[r]:
			l+= 1

	return l-1

def Quickselect(arr, l, r, k):

	if l ==r:
		return arr[l]
	
	try:
		x = np.random.randint(l+1, r)
	except:
		x = np.random.randint(l,r)
	pivot = arr[x]
	m = partition(arr, l, r, pivot)

	if k < m:
		return Quickselect(arr, l, m-1, k)
	elif k > m:
		return Quickselect(arr, m+1, r, k)
	else:
		return arr[k]

if __name__ == "__main__":
	arr = [1, 7, 8, 4, 2, 3, 9, 10]
	k = 3

	t_start = time.time()
	val = Quickselect(arr, 0, len(arr)-1, k)
	duration = round((time.time()- t_start)* 1e3, 5)
	print('Time complexity: '+ str(duration)+ ' ms')

	print(arr)
	print(str(k)+ '-th smallest element is '+ str(val))
