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
    def weighted_matrix(self, Graph_init):
        myMatrix = []
        for vertix in self.Graph_init.keys():
            myMatrix.append(["∞"]*len(self.Graph_init.keys()))
        for key, values in self.Graph_init.items():
            x = key - 1
            for value in values:
                y = value[0] - 1
                myMatrix[x][y] = value[1]
        for row in self.Graph_init.keys():
            for col in self.Graph_init.keys():
                if (row == col):
                    x = row - 1 
                    y = col - 1 
                    myMatrix[x][y] = 0
        
        return myMatrix
    def draw(self, Matrix):
        dbar = '───'*len(self.Graph_init.keys())
        length = self.Graph_init.keys()
        # Print the upper col numbers
        print ('             ',end='  ')
        for col in length: 
            print (col,end='  ')
        print()

        # Print the upper Border.
        print('	   ',"┌─%s─┐"%(dbar))
        # Print a Row.
        for row in range(len(length)):
            print ('	',row+1,' │',end='  ')
        # Print the row content.
            for i in Matrix[row]:
                if (i == "∞"):
                    print('\033[91m%s\033[0m'%("∞"),end='  ')
                elif (i == 0):
                    print('\033[92m%s\033[0m'%(0),end='  ')
                else:
                    print (i,end='  ')
        # Print the row closing bar.
            print ('│  ',end='')
            print()
        print('	   ',"└─%s─┘"%(dbar))
        
def main():
    myGraph = {
        1:[[2,1],[3,2],[7,2],[6,3],[5,5]],
        2:[[1,2],[3,2]],
        3:[[1,2],[2,2],[7,2],[4,3]],
        4:[[3,3],[7,1],[5,1]],
        5:[[4,1],[7,2],[1,5],[6,2]],
        6:[[5,2],[1,3]],
        7:[[1,2],[3,2],[4,1],[5,2]],
    }
    obj = MatricePondiration(myGraph)
    print ("""
	┌───────────────────────────────┐
	│    MATRICE DE PONDIRATION	│
	└───────────────────────────────┘
	""")
    w_matrix = obj.weighted_matrix(myGraph)
    obj.draw(w_matrix)
    
if __name__ == '__main__':
    main()
