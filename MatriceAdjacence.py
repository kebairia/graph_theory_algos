#!/bin/env python
class MatriceAdjacence:
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
        List = []
        for key,values in Graph_init.items():
            if key not in List:
                List.append(key)
            for value in values:
                if value not in List:
                    List.append(value)
        return List
    def or_adj_matrix(self,Graph_init):
        initMarix = []
        for everyVertix in range(self.verticesNumber):
            # to prevent making the row dependet
            initMarix.append(["0"]*self.verticesNumber)
        for index in self.keys:
            for i in Graph_init[index]:
            	initMarix[index-1][i-1] = "1"
        return initMarix
    def nr_adj_matrix(self,Graph_init):
        # Creating the initial Matrix
        initMarix = []
        for everyVertix in range(self.verticesNumber):
        # to prevent making the row dependet
            initMarix.append(["0"]*self.verticesNumber)
        for index in self.keys:
            for i in Graph_init[index]:
            	initMarix[index-1][i-1] = "1"
            	initMarix[i-1][index-1] = "1"
        return initMarix
    def display(self,myMatrix):
        dbar = '───'*self.verticesNumber
#TODO: make the display dynamic with the length of any graph/matrix
        print ('             ',end='  ')
        for everyrow in range(self.verticesNumber):
            print (everyrow+1,end='  ')
        print()
        print('	   ',"┌─%s─┐"%(dbar))
        for everyrow in range(self.verticesNumber):
            print ('	',everyrow+1,' │',end='  ')
            for i in myMatrix[everyrow]:
                print (i,end='  ')
            print ('│  ',end='')
            print()
        print('	   ',"└─%s─┘"%(dbar))
#
#┌───────────────────────────────┐
#│	THE MAIN FUNCTION	 │
#└───────────────────────────────┘
def main():
    myGraph ={
           1:[2,3],
           2:[1,3,5],
           3:[1,2,4,5],
           4:[3,5],
           5:[2,3,4]
                }
    myGraph2 ={
           1:[2,3],
           2:[3,5],
           3:[4],
           4:[5],
           5:[3]
                }
    adj = MatriceAdjacence(myGraph)
    orAdjMatrix = adj.or_adj_matrix(myGraph2)
    nonOrAdjMatrix = adj.nr_adj_matrix(myGraph)
    print ("""
	┌───────────────────────────────┐
	│    ORIENTED ADJANCY MATRIX	│
	└───────────────────────────────┘
	""")
    adj.display(orAdjMatrix)
    print ("""
	┌───────────────────────────────┐
	│  NON ORIENTED ADJANCY MATRIX	│
	└───────────────────────────────┘
	""")
    adj.display(nonOrAdjMatrix)



if __name__ == '__main__':
    main()
