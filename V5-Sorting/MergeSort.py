import numpy as np
import time

# Merge
def Merge(arr, l, m, r):
	B = np.zeros([r-l+1])
	i = l
	j = m+1
	k = 0 # start array to fill at zeroth index

	# compare entries of both arrays until we reach upper end of either one
	while i<= m and j<=r:
		# fill new array with smaller value of either
		if arr[i] <= arr[j]: 
			B[k] = arr[i]
			i+=1
		else:
			B[k] = arr[j]
			j+=1
		k+= 1

	# fill-up new array with remaining of the two array
	while i <= m:
		B[k] = arr[i]
		i+=1
		k+=1
	while j <= r:
		B[k] = arr[j]
		j+=1
		k+=1

	# copy back
	arr[l:r+1] = B.copy()

# MergeSort: recursive
def MergeSort(arr, l, r):
	if l < r:
		m = int((l+r)/2) # Make sure that its an integer
		MergeSort(arr, l, m)
		MergeSort(arr, m+1, r)
		Merge(arr, l, m, r)

# StraightMergeSort: sequential
# basically same procedure as before but avoiding recursion
def StraightMergeSort(arr):
	length = 1
	while length < len(arr): # important to go to len(arr) otw not completely sorted 
		r = -1 # required to start at -1 since indexing starts at 0 (require l=0)
		while r+ length < len(arr):
			l = r+ 1 # makes sure that we cover non-overlapping intervals
			m = l+ length- 1
			r = np.min([m+ length, len(arr)-1]) # right border which is bounded by index = len(arr)-1
			Merge(arr, l, m, r)
		length*= 2 # move in powers of 2

# NaturalMergeSort

if __name__ == "__main__":
	arr = np.array([1, 4, 3, 9, 7, 6, 2, 8, 5])
	print('Unsorter array: '+ str(arr))
	#MergeSort(arr, 0, len(arr)-1) # r = max index = length -1
	StraightMergeSort(arr)
	print('Sorted array: '+ str(arr))
