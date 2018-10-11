#!/bin/env python
#AUTHOR: Kebairia Zakaria
#EMAIL : z.kebairia@esi-sba.dz
#             _  _                     _        _
#    __ _  __| |(_)    _ __ ___   __ _| |_ _ __(_)_  __
#   / _` |/ _` || |   | '_ ` _ \ / _` | __| '__| \ \/ /
#  | (_| | (_| || |   | | | | | | (_| | |_| |  | |>  <
#   \__,_|\__,_|/ |___|_| |_| |_|\__,_|\__|_|  |_/_/\_\
#             |__/_____|
#
class Graph:
    def __init__(self,Graph_init):
        self.edge={}
        for keys,values in Graph_init.items():
             for value in values:
                 self.addEdge(keys,value);
    def addVertex(self,v):
        if v not in self.edge:
            self.edge[v] = []
    
    def addEdge(self,u,v):
        if u not in self.edge:
            self.addVertex(u)
        if v not in self.edge:
            self.addVertex(v)
        if u not in self.edge[v]:
            self.edge[v].append(u)
        if v not in self.edge[u]:
            self.edge[u].append(v)
    
    
    def display(self):
        for keys,values in self.edge.items():
            print(keys,":=>",values)

Graph_init = {1:[2,3,5],
          2:[1,4],
          3:[1,6]};

g=Graph(Graph_init)
g.addVertex(1)
g.addVertex(2) 
g.addVertex(3)
g.addEdge(1,2)
g.addEdge(3,2)
print(g.edge.items())
#vertices = []
#graph = {}
#def addVertex(ver):
    #vertices.append(ver)
#def addEdge(start,end):
    #edge = [start,end]
    #for i in vertices:
       # 
#def graph2or_adj_matrix(myMtrix):
    #for sommet in myMtrix.keys():
    #print(sommet)
       # 
   # 
#
#print('Enter the graph type[or/nr]: ',end='')
#graph_type = input()
#addVertex(1)
#addVertex(2)
#addVertex(3)
#addEdge(1,2)
#addEdge(3,2)
#print(vertices)
#print(graph)
#
