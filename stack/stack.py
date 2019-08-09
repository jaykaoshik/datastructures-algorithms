class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = ListNode(value)
        node.next = self.top
        self.top = node
    def pop(self):
        if(self.top):
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            return float("-inf")
    def peek(self):
        if(self.top):
            return self.top.value
        else:
            return float("-inf")
    def isEmpty(self):
        return (self.top is None)

    def insertAtBottom(self, value):
        if(self.isEmpty()):
            self.push(value)
            return
        val = self.pop()
        self.insertAtBottom(value)
        self.push(val)

    def reverse(self):
        if(self.isEmpty()):
            return
        value = self.pop()
        self.reverse()
        self.insertAtBottom(value)
    def sortedInsert(self, value):
        if(self.isEmpty()):
            self.push(value)
            return
        top = self.peek()
        if(top > value):
            self.push(value)
        else:
            val = self.pop()
            self.sortedInsert(value)
            self.push(val)

    def sort(self):
        if(self.isEmpty()):
            return
        value = self.pop()
        self.sort()
        self.sortedInsert(value)

a = stack()
a.push(1)
a.push(4)
a.push(2)
a.push(5)
a.push(3)
a.sort()
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
