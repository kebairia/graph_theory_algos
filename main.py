#!/bin/python
import graph

def main():
    Graph_init = {1:[2,3,5],
              2:[1,4],
              3:[1,6]};
    
    g=graph.Graph(Graph_init)
    g.addVertex(1)
    g.addVertex(2) 
    g.addVertex(3)
    g.addEdge(1,2)
    g.addEdge(3,2)
    g.addEdge(6,5)
    g.display()
if __name__ == '__main__':
    main()
