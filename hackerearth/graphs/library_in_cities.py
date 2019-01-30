#!/bin/python3

import math
import os
import random
import re
import sys


class Graph:
    def __init__(self):
        self.adjList={}
    def addVertex(self,v):
        if v not in self.adjList:
            self.adjList[v]=[]
            return True
        else:
            return False
    def getVertex(self,v):
        if v in self.adjList:
            return self.adjList[v]
        else:
            return none
    
    def addEdge(self,v1,v2):
        if v1 not in self.adjList:
            n1=self.addVertex(v1)
        if v2 not in self.adjList:
            n2=self.addVertex(v2)
        if v2 not in self.adjList[v1]:
            self.adjList[v1].append(v2)
        if v1 not in self.adjList[v2]:
            self.adjList[v2].append(v1)
        return True
    def connectedComponents(self):
        visited=[False]*len(self.adjList)
        cc=[]

        for v in self.adjList:
            if(visited[v-1]==False):
                temp=[]
                cc.append(self.DFSVisit(visited,v,temp))
        return cc

    def DFSVisit(self,visited,v,temp):
        visited[v-1]=True
        temp.append(v)

        for v1 in self.adjList[v]:
            if visited[v1-1]==False:
                temp=self.DFSVisit(visited,v1,temp)
        return temp
            

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<c_road:
        return n*c_lib
    else:
        price=0
        g=Graph()
        for i in range(n):
            g.addVertex(i+1)
        for i in range(len(cities)):
            g.addEdge(cities[i][0],cities[i][1])
        print('graph==')
        print(g.adjList)
        c=g.connectedComponents()
        for i in range(len(c)):
            l=len(c[i])
            price+=(l-1)*c_road+c_lib
        print(c)
        return price
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
