def nextPermutation():
        """
        Do not return anything, modify nums in-place instead.
        """
        global nums
        def reverse(start, end):
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        length = len(nums)
        
        if(length <= 1):
            return
        first_index = None
        
        #Get the first element that breaks ascending order from the end of the array
        for i in range(length - 2, -1, -1):
            if(nums[i] < nums[i + 1]):
                first_index = i
                break
        
        #No such element. Reverse the array
        if(first_index is None):
            reverse(0, length - 1)
            return
        
        second_index = None
        for i in range(length - 1, -1, -1):
            if(nums[i] > nums[first_index]):
                second_index = i
                break
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        reverse(first_index + 1, length - 1)
        return

import numpy as np
#nums = np.random.randint(20, size = 8)
nums = [3,4,2]
for i in range(20):
    nextPermutation()
    print(nums)