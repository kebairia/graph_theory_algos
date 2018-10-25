#!/usr/bin/env python
class MatriceAdjacence:
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
    def generate_or_adj_matrix(self, Graph_init):
        myMatrix = []
        #Make an iteratble list of edges.
        edges = list(self.generate_edges(self.Graph_init))
        #initialize the matrix
        for vertix in self.Graph_init.keys():
            myMatrix.append([0]*len(self.Graph_init.keys()))
        for i in edges:
            cord = list(i)
            x = cord[0] - 1
            y = cord[1] - 1
            myMatrix[x][y] = 1
        return myMatrix
    def generate_nr_adj_matrix(self, Graph_init):
        myMatrix = []
        #Make an iteratble list of edges.
        edges = list(self.generate_edges(self.Graph_init))
        #initialize the matrix
        for vertix in self.Graph_init.keys():
            myMatrix.append([0]*len(self.Graph_init.keys()))
        for i in edges:
            cord = list(i)
            x = cord[0] - 1
            y = cord[1] - 1
            myMatrix[x][y] = 1
            myMatrix[y][x] = 1
        return myMatrix
    def list_adj(self,Graph_init):
        for key, values in Graph_init.items():
            print('	 ',key,' ',end=' ')
            for value in values:
                print('│→',value,end='')
            print()
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
                print (i,end='  ')
        # Print the row closing bar.
            print ('│  ',end='')
            print()
        print('	   ',"└─%s─┘"%(dbar))
#┌───────────────────────────────┐
#│	      MAIN		 │
#└───────────────────────────────┘
def main():
    myGraph = {
        1:[2,3],
        2:[1,3,5],
        3:[1,2,4,5],
        4:[3,5],
        5:[4,3,2],
        6:[4,3,2,1]
    }
    obj = MatriceAdjacence(myGraph)
    myOrMatrix = obj.generate_or_adj_matrix(myGraph)
    myNrMatrix = obj.generate_nr_adj_matrix(myGraph)
    print ("""
	┌───────────────────────────────┐
	│    ORIENTED ADJANCY MATRIX	│
	└───────────────────────────────┘
	""")
    obj.draw(myOrMatrix)
    print ("""
	┌───────────────────────────────┐
	│  NON ORIENTED ADJANCY MATRIX	│
	└───────────────────────────────┘
	""")
    obj.draw(myNrMatrix)
    print ("""
	┌───────────────────────────────┐
	│         ADJANCY LIST		│
	└───────────────────────────────┘
	""")
    obj.list_adj(myGraph)
if __name__ == '__main__':
    main()
