import numpy as np

def Partition(arr, l, r, pivot):
	# bring elements < pivot to the left
	# bring elements > pivot to the right
	while l <= r:
		while arr[l]< pivot:
			l+= 1
		while arr[r]> pivot:
			r-= 1
		# swap
		temp = arr[l]
		arr[l] = arr[r]
		arr[r] = temp
		
		if arr[l] == arr[r]:
			l+=1
	return l-1

def Pivot(arr, l, r):
	# choose suitable pivot (own function)
	if r-l> 3:
		idx = np.random.randint(l, r, 3)
		return np.median(arr[idx])	
	else:
		idx = l+ int((r-l)/2)
		return arr[idx]

def QuickSort(arr, l, r):
	if l< r:
		# choose pivot (element of array not index!)
		p = arr[l+ int((r-l)/2)]#Pivot(arr, l, r)
		k = Partition(arr, l, r, p)
		QuickSort(arr, l, k-1)
		QuickSort(arr, k+1, r)

if __name__ == "__main__":
	arr = np.array([3, 7, 2, 9, 4, 5, 8])
	print('Unsorted array'+ str(arr))
	QuickSort(arr, 0, len(arr)-1)
	print('Sorted array'+ str(arr))
