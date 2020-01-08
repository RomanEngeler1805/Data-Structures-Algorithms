import time
import numpy as np
import sys

def max_subarr(arr):
	max_summ = 0
	start = 0
	end = 1
	prefix_sum = np.zeros([len(arr)])
	
	t_start = time.time()

	for i in range(1,len(arr)):
		prefix_sum[i] = prefix_sum[i-1]+ arr[i]

	for i in range(1,len(arr)):
		for j in range(1,len(arr)):
			summ = prefix_sum[j]- prefix_sum[i-1]
			if summ > max_summ:
				max_summ = summ
				start = i
				end = j		

	duration = round((time.time() - t_start)* 1e3, 5)	
	print('Run time: '+ str(duration)+ ' ms')	

	return start, end

if __name__ == "__main__":
	arr = np.array([3, 8, -2, 5, -7, 4])

	if len(sys.argv) > 1:
		arr = []
		for num in range(1,len(sys.argv)):
			arr.append(int(sys.argv[num]))
		arr = np.asarray(arr)
		start, end = max_subarr(arr)
	else:
		start, end = max(arr)

	print('Start idx: '+ str(start) + ', End idx: '+ str(end)+ ', Max sum: '+ str(np.sum(arr[start:end+1])))
