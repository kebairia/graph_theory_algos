#!/usr/bin/env python
import bcolors
class MatricePondiration:
# TODO: creat a (pondiration) matrix
# Graph = {
#    4:[1,2],
#    2:[4,3],
#    1:[2,4],
#    3:[1,3]
#    }
# TODO: draw the matrix
    # TODO: 
#┌───────────────────────────────┐
#│	THE CONSTRUCTOR		 │
#└───────────────────────────────┘
    def __init__(self,Graph_init):
        self.keys = Graph_init.keys()
        self.values = Graph_init.values()
        self.vertices = self.vertices(Graph_init)
        
#┌───────────────────────────────┐
#│	THE FUNCTIONS		 │
#└───────────────────────────────┘
# This function return a list of all available vertices
    def vertices(self,Graph_init):
               List = []
               for key, values in Graph_init.items():
                   if key not in List:
                       List.append(key)
                   for value in values:
                       if value not in List:
                           List.append(value)
               return List
# Make the (Matrice Pondiration)
    def pond_matrix(self,Graph_init):
        # Make the initial Matrix
        myMatrix = []	
        for vertix in range(len(self.vertices)):
            myMatrix.append(['∞']*len(self.vertices))
        # Creat the (matrice Pondiration)
        for key in Graph_init:
        # Take the Coordinates of every key
            cord = Graph_init[key]
            x = cord[0]-1
            y = cord[1]-1
            myMatrix[x][y] = key
            myMatrix[y][x] = '∞'
        return myMatrix
        

    def draw(self,myMatrix):
        length = len(self.vertices)
        dbar = '─────'*len(self.keys)
        # Print the col_identifiers
        print('	        ',end='  ')
        for col in range(length):
            print(col+1,end='   ')
        print()
        print('	      ',"┌─%s─┐"%(dbar))
        for x in range(length):
            print ('	   ',x+1,' │',end='  ')
            for y in range(length):
                if (x == y):
                    print ('\033[92m%s\033[0m'%(0),end='   ')
                elif (myMatrix[x][y] == '∞'):
                    print ('\033[91m%s\033[0m'%(myMatrix[x][y]),end='   ')
                else:
                    print (myMatrix[x][y],end='   ')
            print ('│   ',end='')
            print()
        print('	      ',"└─%s─┘"%(dbar))
#┌───────────────────────────────┐
#│	THE MAIN FUNCTION	 │
#└───────────────────────────────┘
def main():
    myGraph ={
           4:[1,2],
           1:[4,3],
           1:[2,3],
           3:[2,5],
           2:[5,3],
                }
    m = MatricePondiration(myGraph)
    l = m.pond_matrix(myGraph)
    print ("""
	    ┌───────────────────────────────┐
	    │    MATRICE DE PONDIRATION     │
	    └───────────────────────────────┘
	""")
    m.draw(l)

if __name__ == '__main__':
    main()
