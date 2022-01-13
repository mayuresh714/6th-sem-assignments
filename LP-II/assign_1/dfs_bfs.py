
class graph:

	def __init__(self):
		self.graph_dict =  {}
		 
	def addEdge(self,u,v):
		if u not in self.graph_dict:
			self.graph_dict[u] = [v]
		else:
			self.graph_dict[u].append(v)
			
		if v not in self.graph_dict:
			self.graph_dict[v] = []


	def BFS(self, s):
		 
		queue         = [s]		 
		visited_nodes = [s]  
		
		while queue:
			s = queue.pop(0)
			for i in self.graph_dict[s]:
				if i not in visited_nodes: 
					queue.append(i)
					visited_nodes.append(i)  
		return self.show(visited_nodes)

	def DFS( self,s):
		stack = [s]
		visited_nodes =  []
		while stack:
			s = stack.pop()
			if s in visited_nodes:
				continue
			visited_nodes.append(s)
			for j in self.graph_dict[s]:
				stack.append(j)

		return self.show(visited_nodes)

	def show(self,lis):
		for i in lis:
			print(i,end = "   ")
		print()

				

			
g = graph()

g.addEdge("a","b")	
g.addEdge("a","c")
g.addEdge('a','m')
g.addEdge('m','k')
g.addEdge("c","g")
g.addEdge("c","e")
g.addEdge("c","f")
g.addEdge("g","h")
g.addEdge("g","i")
g.addEdge("b","d")


#              a
#            / | \
#          /   |   \
#         b     c    m
#        /    / | \    \
#      /     /  |   \    \
#    d      g   e     f    k
#          / \
#         /   \
#        h     i



def menu_driven():
	while True:
		print()
		print("1. Add an edge")
		print("2. BFS")
		print("3. DFS")
		print("4. graph dictionary")
		print("5. Exit")

		choice = int(input("Enter your choice: "))
		if choice == 1:
			u = (input("Enter the first vertex: "))
			v = (input("Enter the second vertex: "))
			g.addEdge(u, v)
		elif choice == 2:
			s = input("Enter the starting vertex: ")
			print("\nBFS traversal: ",end = "")
			g.BFS(s)
		elif choice == 3:
			s = input("Enter the starting vertex: ")
			print("\nDFS traversal: ",end = "")
			g.DFS(s)
		elif choice == 4:
			print(g.graph_dict)
		elif choice == 5:
			break
		else:
			print("Wrong choice")

if __name__ == "__main__":
	menu_driven()