def get_digits(n):
	final = 1
	while(n > 0):
		final = final * (n%10)
		n = n // 10
	return final
def min_K(n):
	i = 1
	while(i<100000):
		if(get_digits(i) == n):
			return i
		i += 1
	return "-1"
import numpy as np
for i in range(10):
	n = np.random.choice(1000,1)
	print(n,min_K(n))