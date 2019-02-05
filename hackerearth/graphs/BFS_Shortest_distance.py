from collections import defaultdict

class Graph:

    def __init__(self,n):
        self.vlist=defaultdict(list)
        for u in range(n):
            self.vlist[u]=[]
    
    def connect(self,u,v):
        self.vlist[u].append(v)
        self.vlist[v].append(u)
    
    def find_all_distances(self,s):
        visited=[False]*len(self.vlist)
        parent=[0]*len(self.vlist)
        distance=[-1]*len(self.vlist)
        Q=[]
        Q.append(s)
        visited[s]=True
        distance[s]=0
        while Q:
            vertex=Q.pop(0)
            
            for v in self.vlist[vertex]:
                if visited[v]==False:
                    visited[v]=True
                    distance[v]=distance[vertex]+6
                    Q.append(v)
        del distance[s]
        for d in distance:
            print(d,end=" ")
        print("")





t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)

