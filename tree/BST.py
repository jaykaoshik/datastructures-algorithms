import queue
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root=None):
        self.root = root
    def insert(self, value):
        def insert_BST(node, value):
            if(node.value > value and not node.left):
                node.left = TreeNode(value)
                return
            if(node.value <= value and not node.right):
                node.right = TreeNode(value)
                return
            if(node.value > value):
                insert_BST(node.left, value)
            else:
                insert_BST(node.right, value)
        if(not self.root):
            self.root = TreeNode(value)
            return
        insert_BST(self.root, value)

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

def pre_to_tree(preorder):
    def recur(preorder, preindex, min, max):
        if(preindex[0] == len(preorder)):
            return None
        value =  preorder[preindex[0]]
        if(value < min or value > max):
            return None
        tree = TreeNode(value)
        preindex[0] = preindex[0] + 1
        print(preindex[0], value)
        tree.left = recur(preorder, preindex, min, value)
        tree.right = recur(preorder, preindex, value, max)
        return tree
    index = [0]
    t = recur(preorder, index, float("-inf"), float("inf"))
    return BST(t)


def pre_to_in(preorder):
    def recur(preorder, preindex, min, max):
        if(preindex[0] == len(preorder)):
            return
        value =  preorder[preindex[0]]
        if(value < min or value > max):
            return
        tree = TreeNode(value)
        preindex[0] = preindex[0] + 1
        print(preindex[0], value)
        tree.left = recur(preorder, preindex, min, value)
        tree.right = recur(preorder, preindex, value, max)
        return tree
    index = [0]
    t = recur(preorder, index, float("-inf"), float("inf"))
    return BST(t)


t = BST()
t.insert(50)
t.insert(40)
t.insert(30)
t.insert(35)
t.insert(65)
t.insert(60)
t.insert(70)
t.print_tree()
preorder = t.get_preorder()
t1 = pre_to_tree(preorder)
t1.print_tree()
