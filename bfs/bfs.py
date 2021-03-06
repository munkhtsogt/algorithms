class Graph():
	
	def __init__(self):
		self.graph = {}

	def addEdge(self, u, v):
		if u not in self.graph:
			self.graph[u] = [v]
		else:
			self.graph[u].append(v)

	def BFS(self, s):
	
		visited = [False] * len(self.graph)
		queue = []
	
		queue.append(s)
		visited[s] = True
	
		while queue:
	
			s = queue.pop(0)
			print s,
		
			for i in self.graph[s]:
				if not visited[i]:
					queue.append(i)
					visited[i] = True
					
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is Breadth First Traversal (starting from vertex 2)"
g.BFS(2)
