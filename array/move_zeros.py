def move_zeros_to_end(arr):
    non_zero_index = -1
    for i in range(len(arr)):
        if(arr[i] != 0):
            non_zero_index += 1
            if(i != non_zero_index):
                arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
    return arr

import numpy as np
N = 10
max_elem = 2
arr = np.random.choice(max_elem, N)
print(arr)
print(move_zeros_to_end(arr))
