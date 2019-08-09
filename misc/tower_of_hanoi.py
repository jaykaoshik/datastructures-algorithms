

def tower_of_hanoi(n,source,des,temp):
	if(n==0):
		return;
	tower_of_hanoi(n-1,source,temp,des)
	print("Move ring " + str(n) + " from "+ str(source) + " to " + str(des))
	tower_of_hanoi(n-1,temp,des,source)

tower_of_hanoi(3,0,2,1)