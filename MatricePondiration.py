#!/usr/bin/env python
class MatricePondiration:
#┌───────────────────────────────┐
#│	THE CONSTRUCTOR		 │
#└───────────────────────────────┘
    def __init__(self,Graph_init):
        self.Graph_init = Graph_init
#┌───────────────────────────────┐
#│	THE FUNCTIONS		 │
#└───────────────────────────────┘
    def vertices(self):
        """ 
        return the vertices of a graph as a list
        """
        return list(self.Graph_init.keys())
    def edges(self):
        """ 
        return a list a all edges of a graph
        """
        return self.generate_edges(self.Graph_init)
    def generate_edges(self, Graph_init):
        edges = []
        for vertix in Graph_init:
            for neighboor in Graph_init[vertix]:
                if {vertix, neighboor} not in edges:
                    edges.append({vertix, neighboor})
        return edges
def main():
    myGraph = {
        
    }
if __name__ == '__main__':
    main()

