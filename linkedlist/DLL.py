class ListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
class DLL:
    def __init__(self, head = None):
        self.head = head
    def insert(self,value):
        temp = ListNode(value)
        temp.next = self.head
        if(self.head):
            self.head.prev = temp
        self.head = temp
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            if(not temp.next):
                last = temp
            temp = temp.next
        print()
        while(last):
            print(last.value, end = " ")
            last = last.prev
        print()
    def create_list(self,arr):
        for i in range(len(arr)):
            self.insert(arr[i])
    def insertAfter(self, node, value):
        temp = ListNode(value)
        next = node.next
        node.next = temp
        temp.prev = node
        if(next):
            next.prev = temp
        temp.next = next
    def insertAt(self, position, value):
        if(position == -1):
            self.insert(value)
            return
        temp = self.head
        for i in range(position):
            temp = temp.next
        self.insertAfter(temp, value)
    def delete(self, node):
        prev = node.prev
        next = node.next
        if(prev):
            prev.next = next
        if(next):
            next.prev = prev

        if(node == self.head):
            self.head = next
        node.prev, node.next = None, None

    def reverse(self):
        temp = self.head
        while(temp):
            temp.prev, temp.next = temp.next, temp.prev
            if(not temp.prev):
                last = temp
            temp = temp.prev
        self.head = last

    def quicksort(self):
        def partition(left, right):
            pivot = right.value
            j = left

            i = left.prev
            while(j!=right):
                if(j.value < pivot):
                    if(not i):
                        i = left
                    else:
                        i = i.next
                    i.value, j.value = j.value, i.value
                j = j.next
            if(not i):
                i = left
            else:
                i = i.next
            i.value, right.value = right.value, i.value
            return i
        def recur(left, right):
            if(left!= right and right!=None and left!= right.next):
                index = partition(left, right)
                recur(left, index.prev)
                recur(index.next, right)
        temp = self.head
        while(temp.next):
            temp = temp.next

        recur(self.head, temp)




a = DLL()
a.create_list([5,7,9,8,2,1])
a.print_list()
a.quicksort()
a.print_list()
