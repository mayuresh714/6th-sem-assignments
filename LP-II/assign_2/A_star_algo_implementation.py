

class Astar:
	def __init__(s):
		s.g = 0
		s.H = 0
		s.path = []
		s.matrix =  [ [ ] ]
		s.neb = {}
		s.start_x , s.start_y , s.goal_x , s.goal_y = 0,0,0,0

	def get_heuristic(s,x1,y1 ):
		x2  = s.goal_x
		y2  = s.goal_y
		return (x1-x2)**2 + (y1-y2)**2

	def valid(s,x,y):
		#print(x,y)
		if  x < 0 or y < 0 or x >= len(s.matrix) or y >= len(s.matrix[0]) or s.matrix[x][y] == -1:
			return False
		else:
			return True

	def get_neighbours(s,x,y):
		neighbours = {}
		move = [[-1,0],[0,-1],[0,1],[1,0]]
		s.g += 1
		for i in move:
			if s.valid(x+i[0],y+i[1]):
				f_val = s.get_heuristic(x+i[0],y+i[1]) + s.g
				neighbours[(x+i[0],y+i[1])] = f_val
		print(x,y, "and",neighbours,"\n")
		return neighbours

	def shortest_path(s,x,y):
		s.path.append((x,y))
		cnt =0
		while s.matrix[x][y] != 2:# and cnt <7:
			s.neb.update(s.get_neighbours(x,y))
			print( s.neb , "\n")
			get_min = min(s.neb,key = s.neb.get)
			s.path.append(get_min)
			s.neb.pop(get_min)
			x = get_min[0]
			y = get_min[1]
			
			print("minimum is ",get_min,"\n")
		 
		print("path is" ,s.path)

obj = Astar()

matrix = [  [ 0,  -1,   0,    0,   0,  0],  
			[ 0,   0,   0,    0,   0,  0], 
			[ 0,  -1,   0,   -1,   0,  0],  
			[ 0,  -1,   0,    0,  -1,  0],
			[ 0,   0,   0,    0,  -1,  2]  ]  

obj.matrix = matrix
obj.start_x = 0
obj.start_y = 0
obj.goal_x = 4
obj.goal_y = 5

obj.shortest_path( obj.start_x , obj.start_y)