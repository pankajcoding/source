from pprint import pprint 
class Vertex:
	def __init__(self, key):
		self.id=key
		self.connectedTo={}

	def addNeighbor(self,nbr,weight=0):
		self.connectedTo[nbr]=weight

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]
class Graph:
	def __init__(self):
		self.vertList={}
	
	def addVertex(self,key):
		vertex=Vertex(key)
		self.vertList[key]=vertex
		return vertex

	def getVertex(self,key):
		if key in self.vertList:
			return self.vertList[key]
		else:
			return None

	def contains(self,key):
		return key in self.vertList

	def addEdge(self,key1,key2,cost=0):
		if key1 not in self.vertList:
			nv1=self.addVertex(key1)
		if key2 not in self.vertList:
			nv2=self.addVertex(key2)
		self.vertList[key1].addNeighbor(key2,cost)
		return True

	def getVertices(self):
		return self.vertList.keys()

	def connectedComponent(self):
		visited=[]
		cc=[]
		for i in range(len(self.vertList)):
			

g=Graph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(4,0,1)
print(g.getVertices())
for x,y in g.vertList.items():
	print(x)
	for w in y:
		print(w)