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

		print(self.graph_dict)
 

	def BFS(self, s):
		visited_nodes = [0] * (max(self.graph_dict) + 1)
		queue = []
		queue.append(s)
		visited_nodes[s] = 1

		while queue:
			s = queue.pop(0)
			print (s, end = " ")
 
			for i in self.graph_dict[s]:
				if visited_nodes[i] == 0:
					queue.append(i)
					visited_nodes[i] = 1

	def DFS(self, s):
		visited_nodes = [0] * (max(self.graph_dict) + 1)
		stack = []
		stack.append(s)
		visited_nodes[s] = 1

		while stack:
			s = stack.pop()
			print (s, end = " ")

			for i in self.graph_dict[s]:
				if visited_nodes[i] == 0:
					stack.append(i)
					visited_nodes[i] = 1
				
 

def menu_driven():
    
    g = graph()

    while True:
        print()
        print("1. Add an edge")
        print("2. BFS")
        print("3. DFS")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            u = int(input("Enter the first vertex: "))
            v = int(input("Enter the second vertex: "))
            g.addEdge(u, v)
        elif choice == 2:
            s = int(input("Enter the starting vertex: "))
            g.BFS(s)
        elif choice == 3:
            s = int(input("Enter the starting vertex: "))
            g.DFS(s)
        elif choice == 4:
            break
        else:
            print("Wrong choice")


if __name__ == '__main__':
    menu_driven()