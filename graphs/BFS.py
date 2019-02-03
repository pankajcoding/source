from collections import defaultdict


class Graph:

	def __init__(self):
		self.adjlist=defaultdict(list)

	def addEdge(self,u,v):
		self.adjlist[u].append(v)

	def BFStraversal(self,s):
		visited=[False]*len(self.adjlist)
		print('visited',visited)
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




g=Graph()
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,2)
g.BFStraversal(0)
print(g.adjlist)