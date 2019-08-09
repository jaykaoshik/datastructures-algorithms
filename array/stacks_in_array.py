import numpy as np
class stack:
	def __init__(prev,data):
		self.prev=prev
		self.val=data

arr=[]
stack_ptr=[-1,-1,-1]
freeIndex=0
def push(stack_num,value):
	lastIndex=stack_ptr[stack_num]
	stack_ptr[stack_num]=freeIndex
	arr.append(stack(lastIndex,value))
	freeIndex+=1

def pop(stack_num):
	lastIndex=stack_ptr[stack_num]
	value=arr[lastIndex].value
	prev=arr[lastIndex].prev
	stack_ptr[stack_num]=prev
	arr[lastIndex]=None
	freeIndex-=1
	return value

