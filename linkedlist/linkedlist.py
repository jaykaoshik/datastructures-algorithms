class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        temp = ListNode(value)
        temp.next = self.head
        self.head = temp

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.value, end = " ")
            temp = temp.next
        print()

    def make_list(self, arr):
        for i in range(len(arr)):
            self.insert(arr[i])


    def delete(self, position):
        if(not self.head):
            return
        temp = self.head

        if(position == 0):
            self.head = temp.next
            temp = None
            return
        for i in range(position - 1):
            temp = temp.next
            if(not temp):
                return
        if(temp.next is None):
            return
        next = temp.next
        temp.next = temp.next.next
        next = None
    def delete_key(self, key):
        temp = self.head
        prev = self.head
        if(not self.head):
            return
        if(temp.value == key):
            self.delete(0)
            return
        temp = temp.next
        while(temp):
            if(temp.value == key):
                next = temp.next
                temp = None
                prev.next = next
                return
            temp = temp.next
            prev = prev.next

    def getNthNode(self, n):
        temp = self.head
        for i in range(n - 1):
            temp = temp.next
            if(not temp):
                return None
        return temp

    def getNthNodeFromLast(self, n):
        temp = self.head
        for i in range(n):
            if(not temp):
                return None
            temp = temp.next

        curr = self.head
        while(temp is not None):
            temp = temp.next
            curr = curr.next
        return curr
    def middle(self):
        slow = self.head
        if(not slow):
            return slow
        fast = slow.next
        if(not fast):
            return slow
        while(fast):
            slow = slow.next
            fast = fast.next
            if(fast):
                fast = fast.next
        return slow

    def detect_loop(self):
        slow = self.head
        if(not slow):
            return False
        fast = slow.next
        if(not fast):
            return False
        while(fast):
            slow = slow.next
            fast = fast.next
            if(fast):
                fast = fast.next
            if(slow == fast):
                return True
        return False

    def isPalin1(self):
        stack = []
        temp = self.head
        while(temp):
            stack.append(temp.value)
            temp = temp.next
        temp = self.head
        print(stack)
        while(stack):
            value = stack.pop()
            if(value != temp.value):
                return False
            temp = temp.next
        return True
    def reverse(self):
        if(not self.head):
            return
        if(not self.head.next):
            return
        prev = None
        curr = self.head
        next = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    def palin2(self):
        middle = self.middle()
        new_list = LinkedList(middle)
        new_list.reverse()
        head2 = new_list.head
        temp = self.head
        while(head2):
            if(head2.value != temp.value):
                return False
            head2 = head2.next
            temp = temp.next
        return True

    def palin3(self):
        def recur_palin(right):
            nonlocal left
            if(right is None):
                return True
            isp = recur_palin(right.next)
            if(not isp):
                return False
            isp_checked = (left.value == right.value)
            left = left.next
            return isp_checked
        left = self.head
        return recur_palin(self.head)
    def remove_dup_sorted(self):
        curr = self.head
        if(not curr):
            return
        next = curr.next
        if(not next):
            return
        while(next):
            if(curr.value == next.value):
                curr.next = next.next
                next = curr.next
            else:
                curr = curr.next
                next = next.next
    def swap_nodes(self, position1, position2):
        if(position1 == position2):
            return
        prev, next, prev1, next1, prev2, next2 = self.head, self.head.next, \
        None, None, None, None
        count1 = 1
        if(position1 == 0):
            prev1 = None
            next1 = self.head
        if(position2 == 0):
            prev2 = None
            next2 = self.head

        while(count1 <= max(position1,position2) and next):
            if(count1 == position1):
                prev1 = prev
                next1 = next
            if(count1 == position2):
                prev2 = prev
                next2 = next
            prev = prev.next
            next = next.next
            if(not next and (not prev1 or not prev2)):
                return
            count1 += 1
        print(next1.value, next2.value)
        if(prev1):
            prev1.next = next2
        else:
            if(next1 == self.head):
                self.head = next2
        if(prev2):
            prev2.next = next1
        else:
            if(next2 == self.head):
                self.head = next1
        next1.next, next2.next = next2.next, next1.next
    def pairwise_swap2(self):
        def recur(prev):
            if(not prev):
                return None
            curr = prev.next
            temp = curr
            if(not curr):
                return prev
            next = curr.next
            curr.next = prev
            prev.next = recur(next)
            return temp
        self.head = recur(self.head)



    def pairwise_swap1(self):
        if(not self.head):
            return
        if(not self.head.next):
            return
        super_prev = ListNode(0)
        prev, curr = self.head, self.head.next
        new_head = self.head.next
        while(prev and curr):
            next = curr.next
            super_prev.next = curr
            curr.next = prev
            prev.next = next
            super_prev = prev
            prev = next
            if(prev):
                curr = prev.next
        self.head = new_head

    def quicksort(self, last = None):
        def partition(head):
            if(not head):
                return None,None
            pivot = head.value
            print(pivot)
            i = head
            j = head
            j = j.next
            prev = head
            while(j != last):
                if(j.value < pivot):
                    prev = i
                    i = i.next
                    i.value, j.value = j.value, i.value
                j = j.next
            return i, prev

        pos, prev = partition(self.head)
        if(not pos):
            return
        pos.value,self.head.value = self.head.value, pos.value
        LinkedList(pos.next).quicksort()
        LinkedList(self.head).print_list()
        self.quicksort(pos)



    def palin_reorder(self):
        front = self.head
        def recur(back):
            nonlocal front
            if(not back):
                return True
            isok = recur(back.next)
            print(front.value, back.value,isok)

            if(isok):
                temp = front.next
                if(temp == back):
                    print("yo")
                    back.next = front
                    front.next = None
                    return False
                front.next = back
                front = back
                front.next = temp
                front = temp
            return isok

        recur(self.head)








import numpy as np
arr = [8,7,6,5,4,3,2,1]
print(arr)
head = LinkedList()
head.make_list(arr)
head.print_list()
head.palin_reorder()
head.print_list()
