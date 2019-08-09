import queue
from heapq import heappush,heappop, heapify
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class tree:
    def __init__(self, root=None):
        self.root = root
    def insert(self, value):
        if(not self.root):
            self.root = TreeNode(value)
            return
        bfs = queue.Queue()
        bfs.put(self.root)
        while(not bfs.empty()):
            length = bfs.qsize()
            for i in range(length):
                curr = bfs.get()
                if(curr.left):
                    bfs.put(curr.left)
                else:
                    curr.left = TreeNode(value)
                    return
                if(curr.right):
                    bfs.put(curr.right)
                else:
                    curr.right = TreeNode(value)
                    return
    def print_tree(self):
        if(not self.root):
            print("None")
            return
        bfs = queue.Queue()
        bfs.put(self.root)
        print(self.root.value)
        while(not bfs.empty()):
            length = bfs.qsize()
            for i in range(length):
                curr = bfs.get()
                if(curr.left):
                    bfs.put(curr.left)
                    print(curr.left.value, end = " ")
                else:
                    print("None", end = " ")
                if(curr.right):
                    bfs.put(curr.right)
                    print(curr.right.value, end = " ")
                else:
                    print("None", end = " ")
            print()
    def print_preorder(self):
        def preorder(node):
            if(not node):
                return;
            print(node.value, end = " ")
            preorder(node.left)
            preorder(node.right)
        preorder(self.root)
        print()
    def print_inorder(self):
        def inorder(node):
            if(not node):
                return;
            inorder(node.left)
            print(node.value, end = " ")
            inorder(node.right)
        inorder(self.root)
        print()
    def print_postorder(self):
        def postorder(node):
            if(not node):
                return;
            postorder(node.left)
            postorder(node.right)
            print(node.value, end = " ")
        postorder(self.root)
        print()

    def get_preorder(self):
        def preorder(node, output):
            if(not node):
                return;
            output.append(node.value)
            preorder(node.left, output)
            preorder(node.right, output)
        output = []
        preorder(self.root, output)
        return output

    def get_inorder(self):
        def inorder(node, output):
            if(not node):
                return;
            inorder(node.left, output)
            output.append(node.value)
            inorder(node.right, output)
        output = []
        inorder(self.root, output)
        return output

    def get_postorder(self):
        def postorder(node, output):
            if(not node):
                return;
            postorder(node.left, output)
            postorder(node.right, output)
            output.append(node.value)
        output = []
        postorder(self.root, output)
        return output

    def get_preorder2(self):
        if(not self.root):
            return []
        curr = self.root
        output = [curr.value]
        stack = [curr]
        while(stack):
            while(curr.left):
                curr = curr.left
                stack.append(curr)
                output.append(curr.value)
            curr = stack.pop()
            if(curr.right):
                curr = curr.right
                stack.append(curr)
                output.append(curr.value)
        return output

    def get_inorder2(self):
        if(not self.root):
            return []
        stack = []
        output = []
        curr = self.root
        stack.append(self.root)
        while(stack):
            while(curr.left):
                curr = curr.left
                stack.append(curr)
            if(stack):
                curr = stack.pop()
                output.append(curr.value)
            else:
                break

            if(curr.right):
                curr = curr.right
                stack.append(curr)
        return output

    def get_postorder2(self):
        if(not self.root):
            return []
        curr = self.root
        output = [curr.value]
        stack = [curr]
        while(stack):
            while(curr.right):
                curr = curr.right
                stack.append(curr)
                output.append(curr.value)
            curr = stack.pop()
            if(curr.left):
                curr = curr.left
                stack.append(curr)
                output.append(curr.value)
        output.reverse()
        return output

    def isSymmetric(self):
        def recur(node1, node2):
            if(not node1 and not node2):
                return True
            if((node1 and not node2) or (not node1 and node2)):
                return False
            if(node1.value != node2.value):
                return False
            return (recur(node1.left, node2.right) and recur(node1.right, node2.left))
        return recur(self.root, self.root)

    def boundary_traversal(self):
        def recur(node, output):
            if(not node):
                return
            recur(node.left, output)
            recur(node.right, output)
            if(not node.left and not node.right):
                output.append(node.value)
        def recur2(node, output):
            if(not node):
                return
            recur2(node.right, output)
            if(node.right):
                output.append(node.value)
        output = []
        temp = self.root
        while(temp.left):
            output.append(temp.value)
            temp = temp.left
        recur(self.root, output)
        recur2(self.root, output)
        return output

    def diagonal_traversal(self):
        priority_queue = []
        node = self.root
        value = 0
        heappush(priority_queue,[value, 0, node])
        length = 1
        while(priority_queue):

            val, len, node = heappop(priority_queue)
            print(node.value)
            if(node.left):
                length += 1
                heappush(priority_queue,[val + 1, length, node.left])
            if(node.right):
                length += 1
                heappush(priority_queue,[val, length, node.right])
    def get_depth(self):
        def recur(node):
            if(not node.left and not node.right):
                return 1
            return max(1+recur(node.left),1+recur(node.right))
        return recur(self.root)
    def make_inorder_dll(self):
        def isleaf(node):
            if(not node):
                return False
            if(node.left is None and node.right is None):
                return True
            else:
                return False
        def make_dll(left, node, right):
            left.right = node
            right.left = node
            return left,right
        def recur(node):
            if(isleaf(node.left) and isleaf(node.right)):
                return make_dll(node.left, node, node.right)
            left_dll = node
            right_end = node
            if(node.left):
                left_dll, left_end = recur(node.left)
                left_end.right = node
                node.left = left_end
            if(node.right):
                right_dll, right_end = recur(node.right)
                node.right = right_dll
                right_dll.left = node
            return left_dll, right_end
        dll, end = recur(self.root)
        return dll







def pre_in_to_tree(preorder, inorder):
    def recur(preorder, inorder, start, end, map):
        if(start >= end - 1):
            return TreeNode(preorder[0])
        root = preorder[0]
        index = map[root] - start
        node = TreeNode(root)
        node.left = recur(preorder[1:index+1], inorder, start, start + index, map )
        node.right = recur(preorder[index+1:], inorder, start + index + 1, end, map)
        return node
    map = {}
    for i in range(len(inorder)):
        map[inorder[i]] = i
    root = recur(preorder, inorder, 0, len(inorder), map)
    return tree(root)



def pre_in_to_post(preorder, inorder):
    def recur(preorder, inorder, start, end, map, output):
        if(start >= end - 1):
            output.append(preorder[0])
            return
        root = preorder[0]
        index = map[root] - start
        recur(preorder[1:index+1], inorder, start, start + index, map, output )
        recur(preorder[index+1:], inorder, start + index + 1, end, map, output)
        output.append(root)
    map = {}
    output = []
    for i in range(len(inorder)):
        map[inorder[i]] = i
    recur(preorder, inorder, 0, len(inorder), map, output)
    return output


def in_post_to_tree(inorder, postorder):
    def recur(inorder, postorder, start, end, map):
        if(start >= end - 1):
            return TreeNode(postorder[-1])
        root = postorder[-1]
        index = map[root] - start
        node = TreeNode(root)
        node.left = recur(inorder, postorder[:index], start, start + index, map )
        node.right = recur(inorder, postorder[index:-1], start + index + 1, end, map)
        return node
    map = {}
    for i in range(len(inorder)):
        map[inorder[i]] = i
    root = recur(inorder, postorder, 0, len(inorder), map)
    return tree(root)




def in_post_to_pre(inorder, postorder):
    def recur(inorder, postorder, start, end, map, output):
        if(start >= end - 1):
            output.append(postorder[-1])
            return
        root = postorder[-1]
        index = map[root] - start
        node = TreeNode(root)
        output.append(root)
        node.left = recur(inorder, postorder[:index], start, start + index, map, output)
        node.right = recur(inorder, postorder[index:-1], start + index + 1, end, map, output)

    map = {}
    output = []
    for i in range(len(inorder)):
        map[inorder[i]] = i
    recur(inorder, postorder, 0, len(inorder), map, output)
    return output

def parent_array_to_tree(parent_array):
    map = {}
    for i in range(len(parent_array)):

        value = parent_array[i]
        if(value == -1):
            if(i not in map):
                map[i] = TreeNode(i)
            root = i
        else:
            if(i not in map):
                map[i] = TreeNode(i)
            if(value not in map):
                map[value] = TreeNode(value)
            if(not map[value].left):
                map[value].left = map[i]
            else:
                map[value].right = map[i]

    return tree(map[root])

def make_tree_from_string(string):
    if(not string):
        return None
    i = 0
    stack = []
    root = None
    while(i < len(string)):
        if(string[i] == ")"):
            stack.pop()
            i += 1
        elif(string[i] == "("):
            i += 1
        else:
            value = int(string[i])
            node = TreeNode(value)
            if(stack):
                if(not stack[-1].left):
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            else:
                root = node
            stack.append(node)
            i += 1
    return tree(root)


t = tree()
t.insert(5)
t.insert(6)
t.insert(7)
t.root.right.left = TreeNode(10)
t.insert(8)
t.insert(9)
t.insert(11)
t.insert(14)
t.insert(15)
t.root.right.left.left = TreeNode(12)
t.root.right.left.right = TreeNode(13)
t.print_tree()
dll = t.make_inorder_dll()
while(dll):
    print(dll.value, end = " ")
    dll = dll.right

abcjjka
print(t.get_depth())
preorder = t.get_preorder()
inorder = t.get_inorder()
postorder2 = t.get_postorder2()
postorder = t.get_postorder()
p = in_post_to_pre(inorder, postorder)
print(postorder, postorder2)
