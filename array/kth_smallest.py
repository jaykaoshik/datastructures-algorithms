def kth_smallest(arr, k):
    # Time complexity: O(n + klogn)
    from heapq import heapify, heappush, heappop
    new_arr = arr.copy()
    heapify(new_arr)
    for i in range(k):
        ans = heappop(new_arr)
    return ans

def kth_smallest_max_heap(arr, k):
    #Time complexity: O(k + (n-k)logk)
    from heapq import heapify, heappush, heappop
    new_arr = [-i for i in arr[:k]]
    heapify(new_arr)
    for i in range(k,len(arr)):
        if(-arr[i] > new_arr[0]):
            new_arr[0] = -arr[i]
            heapify(new_arr)
    return -new_arr[0]

def partition(arr, l ,r):
    pivot = arr[r]
    j = l-1
    for i in range(l,r):
        if(arr[i] < pivot):
            j += 1
            arr[j],arr[i] = arr[i],arr[j]
    j += 1
    arr[j], arr[r] = arr[r], arr[j]
    return j

def quickselect(arr, l, r, k):
    if(k>0 and k<=(r-l+1)):
        pos = partition(arr, l, r)
        if(pos-l == k-1):
            return arr[pos]
        elif(pos-l > k-1):
            return quickselect(arr, l, pos-1, k)
        else:
            return quickselect(arr, pos + 1, r, k-pos+l-1)
def kth_smallest_quick(arr, k):
    new_arr = arr.copy()
    return quickselect(new_arr, 0, len(arr)-1, k)

import numpy as np
N = 10
max_elem = 20
arr = list(np.random.choice(max_elem, N))
print(arr)
for i in range(N):
    print(i+1, kth_smallest_quick(arr, i+1))
arr.sort()
print(arr)
