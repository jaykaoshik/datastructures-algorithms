

import heapq
import os
import math

class graph:
	def __init__(self):
		self.v=[]
		self.edges={}
		self.mat={}
		self.energy={}
	def add_node(self,node):
		self.v.append(node)
		self.edges[node]=[]
	
	def add_edge1(self,node1,node2,weight):
		self.edges[node1].append(node2)
		self.edges[node2].append(node1)
		self.mat[node1+","+node2]=weight
		self.mat[node2+","+node1]=weight
	
	
	def add_edge(self,node1,node2,time,energy):
		self.edges[node1].append(node2)
		self.edges[node2].append(node1)
		self.mat[node1+","+node2]=time
		self.mat[node2+","+node1]=time
		self.energy[node1+","+node2]=energy
		self.energy[node2+","+node1]=energy
	

	def print_graph(self):
		for key in self.edges.keys():
			print(key,self.edges[key])

	def printAllPathsUtil(self, u, d, visited, path, time, energy): 
  
		if(energy>410):
			return
		# Mark the current node as visited and store in path 
		visited[u]= True
		path.append(u)


  
		# If current vertex is same as destination, then print 
		# current path[] 
		if u ==d: 
			print(path,energy,time) 
		else: 
			# If current vertex is not destination 
			#Recur for all the vertices adjacent to this vertex 
			for i in self.edges[u]:
				if i not in visited:
					self.printAllPathsUtil(i, d, visited, path,time+self.mat[u+","+i],energy+self.energy[u+","+i]) 
					  
		# Remove current vertex from path[] and mark it as unvisited 
		path.pop() 
		visited.pop(u, None)
   
   
	# Prints all paths from 's' to 'd' 
	def printAllPaths(self,s, d): 

		# Mark all the vertices as not visited 
		visited ={}

		# Create an array to store paths 
		path = []

		time=0
		energy=0

		# Call the recursive helper function to print all paths 
		self.printAllPathsUtil(s, d,visited, path,time,energy) 

	def bfs_traversal(self,root):
		queue=[]
		queue.append(root)
		visited={}
		for vertex in self.v:
			visited[vertex]=False
		visited[root]=True
		traversal=[]
		while(queue):
			root=queue.pop(0)
			traversal.append(root)
			for vertex in self.edges[root]:
				if(not visited[vertex]):
					queue.append(vertex)
					visited[vertex]=True
		return traversal		

	def bfs_shortest_path(self,source,destination):
		queue=[]
		pred={}
		queue.append(source)
		visited={}
		for vertex in self.v:
			visited[vertex]=False
		visited[source]=True
		pred[source]=None
		found=0
		while(queue):
			curr=queue.pop(0)
			
			for vertex in self.edges[curr]:
				if(not visited[vertex]):
					queue.append(vertex)
					visited[vertex]=True
					pred[vertex]=curr
					if(vertex==destination):
						found=1
						break
			if(found==1):
				break
		path=[]
		curr=destination
		while(curr):
			path.insert(0,curr)
			curr=pred[curr]
		return path

	def neighbors(self,key):
		return self.edges[key]
	def time_matrix(self,str):
		return self.mat[str]
	def energy_matrix(self,str):
		return self.energy[str]



def bidirectional_ucs(graph, start, goal):
	"""
	Exercise 1: Bidirectional Search.

	See README.md for exercise description.

	Args:
		graph (ExplorableGraph): Undirected graph to search.
		start (str): Key for the start node.
		goal (str): Key for the end node.

	Returns:
		The best path as a list from the start and goal nodes (including both).
	"""

	# TODO: finish this function!


	debug=1
	if(start==goal):
		return []

	ucs=[PriorityQueue(),PriorityQueue()]
	curr=[start,goal]
	ucs[0].append([0,start])
	ucs[1].append([0,goal])
	pred=[{},{}]
	pred[0][curr[0]]=None
	pred[1][curr[1]]=None
	visited_nodes=[[curr[0]],[curr[1]]]
	explored_nodes=[{curr[0]},{curr[1]}]
	common_nodes=[]
	value=[{},{}]
	value[0][curr[0]]=0
	value[1][curr[1]]=0
	total_distance=float("inf")  
	i=0

	while((value[0][curr[0]]+value[1][curr[1]])<total_distance):
		
		
		ucs[i].pop()
		if(curr[i] in visited_nodes[1-i]):
			print("Found explored",curr[i])
				
		if(i==1):
			print(curr[i],visited_nodes[1-i])
		if(i==0 and curr[i]=="JEFF"):
			print("Bhag bc",visited_nodes[1])

		for key in graph.neighbors(curr[i]):
			if(key not in visited_nodes[i]):
				explored_nodes[i].add(key)
				new_value=value[i][curr[i]]+graph.time_matrix(curr[i]+","+key)
				key_in_frontier=False

				for node in ucs[i]:
					if(key==node[1]):
						key_in_frontier=True
						if(new_value<value[i][key]):
							value[i][key]=new_value
							node[0]=new_value
							pred[i][key]=curr[i]
				if(key_in_frontier):
					ucs[i].heapify()

				if(not key_in_frontier):
					value[i][key]=value[i][curr[i]]+graph.time_matrix(curr[i]+","+key)
					ucs[i].append([new_value,key])
					pred[i][key]=curr[i]
			

			if(key in explored_nodes[1-i]):
				common_nodes.append(key)
				total_distance=min(total_distance,value[i][curr[i]]+value[1-i][key]+
					graph.time_matrix(curr[i]+","+key))

		curr[i]=ucs[i].top()[1]
		visited_nodes[i].append(curr[i])
		i=1-i

		


	common_key=-1
	min_length=float("inf")
	for key in common_nodes:
		l=value[0][key]+value[1][key]
		if(l<min_length):
			min_length=l
			common_key=key
	
	print("total distance",total_distance)
	if(debug==1):
		print("Common keys:",common_nodes)
		print("Common key:",common_key)
		print("total distance",total_distance)
		print("min_length",min_length)
		print("forward",value[0][key])
		print("backward",value[1][key])
		print("forward values",value[0])
		print("backward values",value[1])

	key=common_key
	path=[]
	path.insert(0,key)
	while(key!=start):
		key=pred[0][key]
		path.insert(0,key)
	
	key=common_key
	while(key!=goal):
		key=pred[1][key]
		path.append(key)

	if(debug==1):
		print(path)

	return path




class PriorityQueue(object):
	"""
	A queue structure where each element is served in order of priority.

	Elements in the queue are popped based on the priority with higher priority
	elements being served before lower priority elements.  If two elements have
	the same priority, they will be served in the order they were added to the
	queue.

	Traditionally priority queues are implemented with heaps, but there are any
	number of implementation options.

	(Hint: take a look at the module heapq)

	Attributes:
		queue (list): Nodes added to the priority queue.
		current (int): The index of the current node in the queue.
	"""

	def __init__(self):
		"""Initialize a new Priority Queue."""

		self.queue = []

	def pop(self):
		"""
		Pop top priority node from queue.

		Returns:
			The node with the highest priority.
		"""

		# TODO: finish this function!

		if(len(self.queue)>=1):
			node=heapq.heappop(self.queue)
			return node

		#raise NotImplementedError

	def remove(self, node_id):
		"""
		Remove a node from the queue.

		This is a hint, you might require this in ucs,
		however, if you choose not to use it, you are free to
		define your own method and not use it.

		Args:
			node_id (int): Index of node in queue.
		"""
		
		size=len(self.queue)
		if(node_id<size and node_id>=0):
			self.queue[node_id]=self.queue[size-1]
			self.queue.pop(size-1)
			heapq.heapify(self.queue)

		#raise NotImplementedError

	def __iter__(self):
		"""Queue iterator."""

		return iter(sorted(self.queue))

	def __str__(self):
		"""Priority Queue to string."""

		return 'PQ:%s' % self.queue

	def append(self, node):
		"""
		Append a node to the queue.

		Args:
			node: Comparable Object to be added to the priority queue.
		"""

		# TODO: finish this function!
		
		heapq.heappush(self.queue,node)

		#raise NotImplementedError

	def __contains__(self, key):
		"""
		Containment Check operator for 'in'

		Args:
			key: The key to check for in the queue.

		Returns:
			True if key is found in queue, False otherwise.
		"""

		return key in [n for _, n in self.queue]

	def __eq__(self, other):
		"""
		Compare this Priority Queue with another Priority Queue.

		Args:
			other (PriorityQueue): Priority Queue to compare against.

		Returns:
			True if the two priority queues are equivalent.
		"""

		return self == other

	def size(self):
		"""
		Get the current size of the queue.

		Returns:
			Integer of number of items in queue.
		"""

		return len(self.queue)

	def clear(self):
		"""Reset queue to empty (no nodes)."""

		self.queue = []

	def top(self):
		"""
		Get the top item in the queue.

		Returns:
			The first item stored in teh queue.
		"""

		return self.queue[0]
	def heapify(self):
		heapq.heapify(self.queue)


a=graph()
a.add_node("SEAT")
a.add_node("PORT")
a.add_node("SANF")
a.add_node("SAND")
a.add_node("BOIS")
a.add_node("LASV")
a.add_node("TUCS")
a.add_node("SALT")
a.add_node("BILL")
a.add_node("CASP")
a.add_node("DENE")
a.add_node("ALBU")
a.add_node("FARG")
a.add_node("RAPI")
a.add_node("GUYM")
a.add_node("SALI")
a.add_node("AUST")
a.add_node("LINC")
a.add_node("ROCH")
a.add_node("JEFF")
a.add_node("LITT")
a.add_node("CHIC")
a.add_node("LOUI")
a.add_node("NASH")
a.add_node("MONT")
a.add_node("ATLA")

# a.add_edge("SEAT","BOIS",217)
# a.add_edge("PORT","BOIS",89)
# a.add_edge("SANF","BOIS",445)
# a.add_edge("BOIS","SALT",246)
# a.add_edge("BOIS","CASP",165)
# a.add_edge("BOIS","BILL",194)
# a.add_edge("SEAT","BILL",158)
# a.add_edge("SANF","LASV",286)
# a.add_edge("SAND","LASV",153)
# a.add_edge("TUCS","LASV",364)
# a.add_edge("LASV","SALT",169)
# a.add_edge("TUCS","DENE",208)
# a.add_edge("TUCS","ALBU",232)
# a.add_edge("SALT","DENE",101)
# a.add_edge("DENE","LINC",314)
# a.add_edge("CASP","LINC",244)
# a.add_edge("DENE","GUYM",144)
# a.add_edge("ALBU","GUYM",130)
# a.add_edge("ALBU","AUST",290)
# a.add_edge("GUYM","AUST",258)
# a.add_edge("DENE","SALI",177)
# a.add_edge("RAPI","FARG",56)
# a.add_edge("RAPI","ROCH",161)
# a.add_edge("FARG","ROCH",310)
# a.add_edge("ROCH","CHIC",169)
# a.add_edge("CASP","ROCH",216)
# a.add_edge("RAPI","BILL",78)
# a.add_edge("BILL","FARG",182)
# a.add_edge("LITT","NASH",300)
# a.add_edge("LITT","MONT",420)
# a.add_edge("MONT","NASH",240)
# a.add_edge("ATLA","MONT",140)
# a.add_edge("NASH","ATLA",230)
# a.add_edge("ATLA","LOUI",360)
# a.add_edge("LOUI","CHIC",159)
# a.add_edge("SAND","TUCS",156)
# a.add_edge("SALT","CASP",67)
# a.add_edge("CASP","RAPI",113)
# a.add_edge("GUYM","LITT",208)
# a.add_edge("SALI","LINC",64)
# a.add_edge("SALI","JEFF",144)
# a.add_edge("SALI","LITT",302)
# a.add_edge("AUST","LITT",259)
# a.add_edge("LINC","ROCH",132)
# a.add_edge("LINC","CHIC",217)
# a.add_edge("LINC","JEFF",97)
# a.add_edge("JEFF","CHIC",131)
# a.add_edge("JEFF","LOUI",335)
# a.add_edge("JEFF","NASH",156)


a.add_edge("SEAT","BOIS",217,55)
a.add_edge("PORT","BOIS",89,57)
a.add_edge("SANF","BOIS",445,110)
a.add_edge("BOIS","SALT",246,77)
a.add_edge("BOIS","CASP",165,57)
a.add_edge("BOIS","BILL",194,44)
a.add_edge("SEAT","BILL",158,37)
a.add_edge("SANF","LASV",286,54)
a.add_edge("SAND","LASV",153,49)
a.add_edge("TUCS","LASV",364,95)
a.add_edge("LASV","SALT",169,46)
a.add_edge("TUCS","DENE",208,130)
a.add_edge("TUCS","ALBU",232,71)
a.add_edge("SALT","DENE",101,72)
a.add_edge("DENE","LINC",314,87)
a.add_edge("CASP","LINC",244,102)
a.add_edge("DENE","GUYM",144,40)
a.add_edge("ALBU","GUYM",130,66)
a.add_edge("ALBU","AUST",290,87)
a.add_edge("GUYM","AUST",258,77)
a.add_edge("DENE","SALI",177,40)
a.add_edge("RAPI","FARG",56,25)
a.add_edge("RAPI","ROCH",161,70)
a.add_edge("FARG","ROCH",310,70)
a.add_edge("ROCH","CHIC",169,61)
a.add_edge("CASP","ROCH",216,100)
a.add_edge("RAPI","BILL",78,26)
a.add_edge("BILL","FARG",182,80)
a.add_edge("LITT","NASH",300,90)
a.add_edge("LITT","MONT",420,120)
a.add_edge("MONT","NASH",240,70)
a.add_edge("ATLA","MONT",140,40)
a.add_edge("NASH","ATLA",230,60)
a.add_edge("ATLA","LOUI",360,100)
a.add_edge("LOUI","CHIC",159,52)
a.add_edge("SAND","TUCS",156,58)
a.add_edge("SALT","CASP",67,32)
a.add_edge("CASP","RAPI",113,26)
a.add_edge("GUYM","LITT",208,108)
a.add_edge("SALI","LINC",64,30)
a.add_edge("SALI","JEFF",144,40)
a.add_edge("SALI","LITT",302,122)
a.add_edge("AUST","LITT",259,85)
a.add_edge("LINC","ROCH",132,65)
a.add_edge("LINC","CHIC",217,68)
a.add_edge("LINC","JEFF",97,40)
a.add_edge("JEFF","CHIC",131,48)
a.add_edge("JEFF","LOUI",335,85)
a.add_edge("JEFF","NASH",156,65)




#a.print_graph()

#a.printAllPaths("ATLA","SEAT")
#print(a.bfs_traversal("1"))
#print(a.bfs_shortest_path("1","7"))		
print(bidirectional_ucs(a,"ATLA","SEAT"))
#print(bidirectional_ucs(a,"ATLA","SAND"))