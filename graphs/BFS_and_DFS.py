from collections import defaultdict


class Graph:

	def __init__(self):
		self.adjlist=defaultdict(list)

	def addEdge(self,u,v):
		self.adjlist[u].append(v)

	def BFStraversal(self,s):
		visited=[False]*len(self.adjlist)
		Q=[]
		Q.append(s)
		while(len(Q)!=0):
			vertex=Q.pop(0)
			visited[vertex]=True
			print(vertex,end="-->")
			neighbours=self.adjlist[vertex]
			for v in neighbours:
				if visited[v]==False:
					Q.append(v)

	def DFStraversal(self,s):
		visited=[False]*len(self.adjlist)
		stack=[]
		visited[s]=True
		stack.append(s)
		while stack:
			# print('stack',stack)
			vertex=stack.pop()
			print(vertex,end="-->")
			for v in self.adjlist[vertex]:
				if visited[v]==False:
					visited[v]=True
					stack.append(v)




g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,2)
print(g.adjlist)
print('BFS')
g.BFStraversal(0)
print('DFS')
g.DFStraversal(0)
