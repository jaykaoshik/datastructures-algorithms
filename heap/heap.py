max_size = 10000
import numpy as np
class heap:
    def __init__(self):
        self.arr = np.zeros((max_size,), dtype = int)
        self.size = 0
    def heappush(self, value):
        self.arr[self.size] = value
        self.heapify_up(self.size)
        self.size += 1

        print(self.arr[:self.size])

    def heapify(self, value):
        curr = value
        while(curr < self.size):
            smallest = curr
            if(2*curr + 1 < self.size):
                if(self.arr[2*curr + 1] < self.arr[smallest]):
                    smallest = 2*curr + 1
            if(2*curr + 2 < self.size):
                if(self.arr[2*curr + 2] < self.arr[smallest]):
                    smallest = 2*curr + 2

            if(curr != smallest):
                self.arr[curr], self.arr[smallest] = self.arr[smallest], self.arr[curr]
                curr = smallest
            else:
                break
    def heapify_up(self, value):
        curr = value
        while(curr >= 0):
            smallest = curr
            parent = (curr - 1)//2
            if(parent >= 0):
                if(self.arr[parent] > self.arr[curr]):
                    self.arr[curr], self.arr[parent] = self.arr[parent], self.arr[curr]
                    curr = parent
                else:
                    break
            else:
                break
    def heappop(self):
        value = self.arr[0]
        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]

        self.size -= 1
        self.heapify(0)
        print(self.arr[:self.size])
        return value


a = heap()
a.heappush(5)
a.heappush(8)
a.heappush(7)
a.heappush(1)
a.heappush(10)
a.heappush(2)
print(a.heappop())
print(a.heappop())
print(a.heappop())
print(a.heappop())
