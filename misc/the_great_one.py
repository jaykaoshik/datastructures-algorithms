#code
def isPrime(n):
    if(n == 1):
        return False
    m = n
    while(m % 2 == 0):
        m = m / 2
        if(m > 1):
            return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if(m % i == 0):
            m = m / i
            if(m > 1):
                return False
    return True
import math
T = int(input())
inf = 1e18 + 1
while(T > 0):
    num_elems = int(input())
    arr = input().split(" ")
    new_arr = []
    for i in range(num_elems):
        N = int(arr[i])
        sqrt = math.sqrt(N)
        if(sqrt % 1 == 0):
            if(isPrime(int(sqrt))):
                a = [inf for j in range(19)]
                cnt = 0
                while(N > 0):
                    digit = N % 10
                    a[cnt] = digit
                    cnt += 1
                    N = N // 10
        
                a[:cnt] = a[:cnt][::-1]
                
                new_arr.append(a)
    
    new_arr = sorted(new_arr, reverse = True)
    
    
    for i in range(len(new_arr)):
        temp = new_arr[i]
        j = 0
        while(temp[j] < 1e18):
            print(temp[j],end="")
            j = j + 1
                
    print()
    T -= 1