#!/usr/bin/env python
import bcolors
class MatricePondiration:
#┌───────────────────────────────┐
#│	THE CONSTRUCTOR		 │
#└───────────────────────────────┘
    def __init__(self,Graph_init):
        self.keys = Graph_init.keys()
        self.values = Graph_init.values()
        self.vertices = self.vertices(Graph_init)
        # Sort the vertices
        self.vertices.sort()
        
#┌───────────────────────────────┐
#│	THE FUNCTIONS		 │
#└───────────────────────────────┘
# This function return a list of all available vertices
    def info(self,Graph_init):
        print ('\033[93m%s\033[0m : %d'%('ORDRE DE GRAPH:',len(self.vertices)))
        print ('\033[93m%s\033[0m : %s'%('V:',self.vertices))
        print ('\033[93m%s\033[0m : %s'%('E:',list(self.values)))
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
        for weight,cord in Graph_init.items():
        # Take the Coordinates of every key
        # key == weight
        # cord == values
        # FIXME: if two keys have the same id, the prog will take the last one
        #         and overwrite all the rest 
            x = cord[0]-1
            y = cord[1]-1
            myMatrix[x][y] = weight
            myMatrix[y][x] = weight

        return myMatrix

    def draw(self,myMatrix):
        print ()
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
           1:[2,3],
           1:[4,3],
           3:[2,5],
           2:[5,3],
                }
    obj = MatricePondiration(myGraph)
    matrix = obj.pond_matrix(myGraph)
    obj.info(myGraph)
    print ("""
	    ┌───────────────────────────────┐
	    │    MATRICE DE PONDIRATION     │
	    └───────────────────────────────┘
	""")
    obj.draw(matrix)

if __name__ == '__main__':
    main()
