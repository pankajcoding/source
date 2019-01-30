class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.vertexList={}

	def addVertex(self,vertex):
		if vertex not in self.vertexList: 
			self.vertexList[vertex]=[]
			return self.vertexList[vertex]
		else:
			return self.vertexList[vertex]

	def getVertex(self,vertex):
		if vertex in self.vertexList:
			return self.vertexList[vertex]
		else:
			return None

	def addEdge(self,v1,v2):
		if v1 not in self.vertexList:
			n1=self.addVertex(v1)
		if v2 not in self.vertexList:
			n1=self.addVertex(v2)
		if v2 not in self.vertexList[v1]:
			self.vertexList[v1].append(v2)
		if v1 not in self.vertexList[v2]:
			self.vertexList[v2].append(v1)
		return True

	def getEdgeList(self,v):
		if v in self.vertexList:
			return self.vertexList[v]

	def printGraph(self):
		print(self.vertexList)
		# for x,y in self.vertexList:
		# 	print(x,y)
	def connectedComponent(self):
		visited=[False]*len(self.vertexList)
		print(visited)
		cc=[]
		for v in self.vertexList:
			if(visited[v-1]==False):
				temp=[]
				cc.append(self.DFSVisit(temp,v,visited))
		return cc

	def DFSVisit(self,temp,v,visited):
		visited[v-1]=True
		temp.append(v)
		print('calling',v)
		for v in self.vertexList[v]:
			if visited[v-1]==False:
				temp=self.DFSVisit(temp,v,visited)
		return temp



g=Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(2,4)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(5,6)
g.printGraph()
print(g.getEdgeList(1))
print(g.connectedComponent())