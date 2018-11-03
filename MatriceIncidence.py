#!/bin/env python
import os
class MatriceIncidence:
#┌───────────────────────────────┐
#│	THE CONSTRUCTOR		 │
#└───────────────────────────────┘
    def __init__(self,Graph_init):
        self.keys = list(Graph_init.keys())
        self.values = list(Graph_init.values())
        self.verticesNumber = len(self.vertices(Graph_init))
#┌───────────────────────────────┐
#│	THE FUNCTIONS		 │
#└───────────────────────────────┘
    def vertices(self,Graph_init):
        list_of_vertices = []
        for values in Graph_init.values():
            for value in values:
                if value not in list_of_vertices:
                    list_of_vertices.append(value)
        return list_of_vertices

    def ind_matrix(self,Graph_init):
        initMatrix = []
        #tmp graph for iterating uses
        myGraph = {}
        for i in range(len(self.keys)):
            myGraph[i+1] = self.values[i]
        #Creat the initial Matrix
        for i in range(len(self.vertices(Graph_init))):
            initMatrix.append([" 0"]*len(self.keys))
        #Creating the incedence matrix
        for key, values in myGraph.items():
            initMatrix[values[0]-1][key-1] = " 1" 
            initMatrix[values[1]-1][key-1] = '-1'
        return initMatrix
    # FIXME: the prg is restricted to a dict with sorted key label
    #		must fix this even if the graph given was not a key sorted.
            
    def display(self,myMatrix):
        dbar = '────'*len(self.keys)
#TODO: make the display dynamic with the length of any graph/matrix
        print ('              ',end='  ')
        for everyrow in self.keys:
            print (everyrow,end='   ')
        print()
        print('	   ',"┌─%s─┐"%(dbar))
        for everyrow in range(self.verticesNumber):
            print ('	',everyrow+1,' │',end='  ')
            for i in myMatrix[everyrow]:
                print (i,end='  ')
            print ('│  ',end='')
            print()
        print('	   ',"└─%s─┘"%(dbar))

        
#┌───────────────────────────────┐
#│	THE MAIN FUNCTION	 │
#└───────────────────────────────┘
def main():
    myGraph ={
           "A":[1,2],
           "B":[1,3],
           "C":[2,3],
           "D":[2,5],
           "E":[5,3],
           "F":[3,4],
           "G":[4,5]
                }
    adj = MatriceIncidence(myGraph)
    ind = adj.ind_matrix(myGraph)
    print ("""
	    ┌───────────────────────────────┐
	    │        INCEDENCE MATRIX       │
	    └───────────────────────────────┘
	""")
    adj.display(ind)



if __name__ == '__main__':
    main()
