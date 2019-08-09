#Recursive
def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if(len(nums) == 0):
        return [[]]
    if(len(nums) == 1):
        return [nums]
    output = []
    for i in range(len(nums)):
        first = nums[i]
        rest = nums[:i].copy() + nums[i+1:].copy() 
        for arr in self.permute(rest):
            output.append([first] + arr)
    return output


def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                # if i<len(perm) and perm[i]==n: 
                #     break
        perms = new_perms
    return perms