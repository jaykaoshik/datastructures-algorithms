def binary_search(arr, target):
	start=0
	end=len(arr)
	while(start < end):
		mid = (start + end) //2
		if(arr[mid] >= target):
			end = mid
		else:
			start = mid + 1

	return start