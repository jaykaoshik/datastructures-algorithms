def next_greater_number(n):
    pivot1 = -1
    if(len(n) <= 1):
        return n

    for i in range(len(n) - 1, 0, -1):
        if(n[i -1] < n[i]):
            pivot1 = i -1
            break

    if(pivot1 == -1):
        return n
    pivot2 = -1

    for i in range(pivot1 + 1, len(n)):
        if(n[i] <= n[pivot1]):
            pivot2 = i - 1
            break

    if(pivot2 == -1):
        pivot2 = len(n) - 1
    n[pivot1], n[pivot2] = n[pivot2], n[pivot1]

    start = pivot1 + 1
    end = len(n) - 1
    while(start < end):
        n[start], n[end] = n[end], n[start]
        start += 1
        end -= 1
    return n
# start_arr = [1,1,2,2,3,4,5]
# for i in range(15):
#     print(next_greater_number(start_arr))
def my_func(s,total):
    def recur(n):
        nonlocal s
        if(n == total):
            return
        s = "*" + s + "*"
        recur(n + 1)
    recur(0)
    return s
print(my_func("I am a pro", 10))
