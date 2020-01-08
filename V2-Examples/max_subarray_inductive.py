import time
import numpy as np
import sys

def max_subarr(arr):
	max_summ = 0
	summ = 0
	
	t_start = time.time()

	for i in range(len(arr)):
		summ += arr[i]
		if summ < 0:
			summ = 0
		if summ > max_summ :
			max_summ = summ		

	duration = round((time.time() - t_start)* 1e3, 5)	
	print('Run time: '+ str(duration)+ ' ms')	

	return max_summ

if __name__ == "__main__":
	arr = np.array([3, 8, -2, 5, -7, 4])

	if len(sys.argv) > 1:
		arr = []
		for num in range(1,len(sys.argv)):
			arr.append(int(sys.argv[num]))
		arr = np.asarray(arr)
		summ = max_subarr(arr)
	else:
		summ = max_subarr(arr)

	print('Max sum: '+ str(summ))
