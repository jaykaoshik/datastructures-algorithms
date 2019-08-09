def binary_search(arr, element):
    start = 0
    end = len(arr)
    while(start < end):
        mid = (start +  end) // 2
        if(element == arr[mid]):
            return True
        elif(element < arr[mid]):
            end = mid
        elif(element > arr[mid]):
            start = mid + 1
    return False
def recursive_binary_search(arr, element):
    if(len(arr) == 0):
        return False
    mid = len(arr) // 2
    if(arr[mid] == element):
        return True
    elif(arr[mid] < element):
        return recursive_binary_search(arr[mid+1:], element)
    else:
        return recursive_binary_search(arr[:mid], element)
        
import numpy as np
N = 10
max_elem = 20
arr = np.random.choice(max_elem, N)
arr.sort()
print(arr)
for i in range(len(arr)):
    print(arr[i], recursive_binary_search(arr, arr[i]))

for i in range(N):
    elem = np.random.choice(max_elem, 1)[0]
    print(elem,recursive_binary_search(arr, elem))
