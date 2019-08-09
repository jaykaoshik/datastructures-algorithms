class tree_node:
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data



'''
def print_tree(root):
	
	if(root is None):
		print("None")
		return

	queue=[]
	queue.append(root)

	while(len(queue)>0):
		root=queue.pop(0)
		
		if(root.left or root.right):
			if(root.left):
				queue.append(root.left)
			else:
				queue.append(tree_node("None"))
			if(root.right):
				queue.append(root.right)
			else:
				queue.append(tree_node("None"))
			print(root.data)
			print("Queue:")
			for val in queue:
				print(val.data)
'''


def get_height(root):
	
	if(root is None):
		return 0

	queue=[]
	queue.append(root)
	h=0

	while(len(queue)>0):
		node_count=len(queue)
		h=h+1
		while(node_count>0):
			node=queue.pop(0)
			if(node.left):
				queue.append(node.left)
			if(node.right):
				queue.append(node.right)
			node_count=node_count-1

	return h


def print_tree(root):
	
	if(root is None):
		print("None")

	queue=[]
	queue.append(root)
	height=get_height(root)
	print(height)
	h=0


	while(h<height and len(queue)>0):
		node_count=len(queue)
		h=h+1
		for val in queue:
			print(val.data,end=" ")
		print()

		
		while(node_count>0):
			node=queue.pop(0)
			if(node.left):
				queue.append(node.left)
			else:
				queue.append(tree_node(None))
			if(node.right):
				queue.append(node.right)
			else:
				queue.append(tree_node(None))
			node_count=node_count-1





def preorder(root,order):
	order.append(root.data)

	if(root.left):
		preorder(root.left,order)
	
	if(root.right):
		preorder(root.right,order)
	return order


def inorder(root,order):
	if(root.left):
		inorder(root.left,order)
	order.append(root.data)
	if(root.right):
		inorder(root.right,order)
	return order


def postorder(root,order):
	if(root.left):
		postorder(root.left,order)
	
	if(root.right):
		postorder(root.right,order)
	order.append(root.data)
	return order


def pre_in_to_post(pre_order,in_order,length,order):
	root=in_order.index(pre_order[0])
	if(root!=0):
		pre_in_to_post(pre_order[1:],in_order,root,order)
	if(root!=(length-1)):
		pre_in_to_post(pre_order[root+1:],in_order[root+1:],length-root-1,order)
	order.append(pre_order[0])
	return order



def search(root,key,arr,level):
	if(root.data==key):
		arr[level]=key
		return arr
	if(root.left):
		arr[level]=root.data
		search(root.left,key,arr,level+1)

	if(root.right):
		arr[level]=root.data
		search(root.right,key,arr,level+1)

	return arr


def print_paths_root_to_leaf(root,path):

	path.append(root.data)
	import copy
	path_copy=copy.copy(path)
	
	if(root.left is None and root.right is None):
		print(path)

	if(root.left):
		print_paths_root_to_leaf(root.left,path)
	if(root.right):
		print_paths_root_to_leaf(root.right,path_copy)
		
def insert_BST(root,key):

	if(root is None):
		root=tree_node(key)
		return root
	if(root.data<key):
		if(root.right):
			insert_BST(root.right,key)
		else:
			root.right=tree_node(key)
	else:
		if(root.left):
			insert_BST(root.left,key)
		else:
			root.left=tree_node(key)
	return root


def delete(root,key):
	if(key<root.data):
		if(root.left):
			delete(root.left,key)
		else:
			return "Not Found"
	elif(key>root.data):
		if(root.right):
			delete(root.right,key)
		else:
			return "Not Found"
	else:
		if(root.left is None )

'''
root=tree_node(1)
root.right=tree_node(3)
right=root.right
right.left=tree_node(2)
right.right=tree_node(4)
right.left.right=tree_node(5)
'''

root=None
root=insert_BST(root,10)
root=insert_BST(root,6)
root=insert_BST(root,12)
root=insert_BST(root,1)
root=insert_BST(root,8)
root=insert_BST(root,7)
root=insert_BST(root,9)
root=insert_BST(root,11)
root=insert_BST(root,16)
print_tree(root)

print_paths_root_to_leaf(root,[])

#print(search(root,4,{},0))

#print(get_height(root))

'''
pre_order=preorder(root,[])
in_order=inorder(root,[])
print("Pre order",pre_order)
print("In order",in_order)
post_order=pre_in_to_post(pre_order,in_order,len(in_order),[])
print(post_order)
'''

#print_tree(root)



