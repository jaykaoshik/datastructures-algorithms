import numpy as np
import timeit
def bubble_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if(arr[j]>arr[j+1]):
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr


def merge(arr1,arr2):
	i=j=0
	arr=[]
	while(i<len(arr1) and j<len(arr2)):
		if(arr1[i]<arr2[j]):
			arr.append(arr1[i])
			i+=1
		else:
			arr.append(arr2[j])
			j+=1
	while(i<len(arr1)):
		arr.append(arr1[i])
		i+=1
	while(j<len(arr2)):
		arr.append(arr2[j])
		j+=1
	return arr

def merge_sort(arr):

	l=len(arr)
	if(l==1):
		return arr
	mid=(l)//2

	left=merge_sort(arr[0:mid])
	right=merge_sort(arr[mid:l])
	return merge(left,right)


def quick_sort(arr,start,end):
	if(start>=end):
		return
	
	pivot=arr[end]
	i=start-1
	j=start
	while(j<end):
		if(arr[j]>pivot):
			j+=1
		else:
			i+=1
			arr[i],arr[j]=arr[j],arr[i]
			j+=1
	i+=1
	arr[i],arr[end]=arr[end],arr[i]
	quick_sort(arr,start,i-1)
	quick_sort(arr,i+1,end)
	



a=[88,6,22,971,9,10,4,435,25]
'''
quick_sort(a,0,len(a)-1)
print(a)
'''

def heapify(arr,i,n):
	parent=arr[i]
	largest=i
	l=i*2+1
	if(l<n):
		if(arr[largest]<arr[l]):
			largest=l
	r=i*2+2
	if(r<n):
		if(arr[largest]<arr[r]):
			largest=r
	if(largest!=i):
		arr[largest],arr[i]=arr[i],arr[largest]
		heapify(arr,largest,n)


def heapsort(arr):
	n=len(arr)-2
	for i in range(n//2,-1,-1):
		heapify(arr,i,len(arr))
	n=len(arr)-1
	for i in range(n,0,-1):
		arr[0],arr[i]=arr[i],arr[0]
		heapify(arr,0,i)

'''
heapsort(a)
print(a)
'''
def getdigit(n,index):
	for key in range(index+1):
		digit=n%10
		n=int(n/10)
	return digit



def list_to_buckets(num_list,index):
	num_dict={}
	for num in num_list:
		digit=getdigit(num,index)
		if(digit in num_dict):
			num_dict[digit].append(num)
		else:
			num_dict[digit]=[num]
	return num_dict

def buckets_to_list(buckets):
	output=[]
	for key in sorted(buckets.keys()):
		for num in buckets[key]:
			output.append(num)
	return output 

def radix_sort(arr):
	max_digits=0
	for num in arr:
		temp=num
		count=0
		while(temp>0):
			temp=int(temp/10)
			count+=1
		max_digits=max(max_digits,count)

	for index in range(max_digits):
		arr=buckets_to_list(list_to_buckets(arr,index))
	return arr		


print(radix_sort(a))

