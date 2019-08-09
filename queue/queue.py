class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if(not root):
        return
    bfs = []
    bfs.insert(0,root)
    while(len(bfs)>0):
        length = len(bfs)
        curr = None
        for i in range(length):
            prev = curr
            curr = bfs.pop()
            if(prev):
                prev.next = curr
            if(curr.left):
                bfs.insert(0,curr.left)
            if(curr.right):
                bfs.insert(0,curr.right)
        curr.next = None


def connect2(root):
    if(not root):
        return
    
    while(root):
        temp = TreeLinkNode(0)
        curr = temp
        while(root):
            if(root.left):
                curr.next = root.left
                curr = curr.next
            if(root.right):
                curr.next = root.right
                curr = curr.next
            root = root.next
        root = temp.next
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.right = TreeLinkNode(7)

connect2(root)
print(root.next)
print(root.left.next.val)
print(root.left.left.next.val)
print(root.left.right.next.val)
