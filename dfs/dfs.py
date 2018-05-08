class Graph():
	def __init__(self):
		self.graph = {}
	
	def addEdge(self, u, v):
		if u not in self.graph:
			self.graph[u] = [v]
		else:
			self.graph[u].append(v)
	
	def DFSUtil(self, s, visited):
		
		visited[s] = True
		print s,
		
		for i in self.graph[s]:
			if not visited[i]:
				self.DFSUtil(i, visited)
	
	def DFS(self, s):
		
		visited = [False] * len(self.graph)
		self.DFSUtil(s, visited)
	
	def dfs(self, s):
		visited, stack = set(), [s]
		while stack:
			vertex = stack.pop()
			if vertex not in visited:
				print vertex,
				visited.add(vertex)
				
			for v in self.graph[vertex]:
				if v not in visited:
					stack.append(v)
						

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print "Following is DFS from (starting from vertex 2)"
g.dfs(2)
