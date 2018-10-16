!/bin/env python
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
    
    def calculateLength(self):
        l = len(self.edge.keys())
        return l
    
    def display(self):
        for keys,values in self.edge.items():
            print(keys,":=>",values)
