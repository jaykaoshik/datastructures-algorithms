import numpy as np
class kStacks:
    def __init__(self, k):
        self.arr = [-1 for i in range(100)]
        self.free = 0
        self.top = [-1 for i in range(k+1)]
        self.next = np.arange(100) + 1
    def push(self, value, stack_number):
        idx = self.free
        self.free = self.next[idx]
        self.next[idx] = self.top[stack_number]
        self.top[stack_number] = idx
        self.arr[idx] = value
        print("Pushed ",value," to ",stack_number)
    def pop(self, stack_number):
        idx = self.top[stack_number]
        if(idx == -1):
            raise ValueError("Stack empty!")
        value = self.arr[idx]
        self.top[stack_number] = self.next[idx]
        self.next[idx] = self.free
        self.free = idx
        print("Popped ",value,"  from ",stack_number)


stacks = kStacks(3)
while(True):
    response = input("Push(1) or pop(2)? ")
    if(response == "1"):
        value = input("Enter value: ")
        stack_number = input("Enter stack_number: ")
        stacks.push(int(value), int(stack_number))
        print("Arr:", stacks.arr)
    elif(response == "2"):
        stack_number = input("Enter stack_number: ")
        stacks.pop(int(stack_number))
        print("Arr:", stacks.arr)
