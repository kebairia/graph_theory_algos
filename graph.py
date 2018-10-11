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

