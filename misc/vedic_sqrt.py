class Solution:
    def duplex (self, x):
        
        start = 0
        end = len(x) -1
        sum = 0
        while(start < end):
            sum += (2*x[start]*x[end])
            start += 1
            end -= 1
        if(start == end):
            sum += x[start]*x[end]
        return sum
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        num_digits = 0
        temp = x
        list_digits = []
        if(x == 0):
            return 0
        while(temp > 0):
            list_digits = [temp%10] + list_digits  
            temp = temp//10
            num_digits+=1
        if(num_digits % 2 == 1):
            start = list_digits[0]
            index = 1
        else:
            start = list_digits[0]*10 + list_digits[1]
            index = 2
        
        d = 0
        while(d*d <= start):
            d += 1
        d-=1
        divisor = d*2
        duplex_list = []
        result_digits = (num_digits + 1) // 2
        r = start - d*d
        q = d
        result = result * 10 + q
        result_digits -= 1
        
        while(index < len(list_digits) and result_digits > 0):
            print(q,r,list_digits[index])
            start = r*10 + list_digits[index]
            q, r = divmod(start - self.duplex(duplex_list), divisor) 
            duplex_list.append(q)
            result = result * 10 + q
            result_digits -= 1
            index += 1
        return result