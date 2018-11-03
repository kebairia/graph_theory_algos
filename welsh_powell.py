#!/usr/bin/env python
# TODO: make the code more readble
class Welsh_Powell:
    def __init__(self,Graph_init):
        """ Note that this algorithme can't assure that the number of color is the minimum"""
        self.Graph_init = Graph_init

    def color_nodes(self):
        graph = self.Graph_init
        color_map = {}
        # Order the nodes
        nodes = sorted(list(graph.keys()), key=lambda x: len(graph[x]), reverse = True)
        for node in nodes:
            available_colors = [True] * len(nodes)
            for neighbor in graph[node]:
                if neighbor in color_map:
                    color = color_map[neighbor]
                    available_colors[color] = False
            for color, available in enumerate(available_colors):
                if available:
                    color_map[node] = color
                    break
        return color_map
    def chromatic_number(self):
        color_map = self.color_nodes()
        chr_nbr = set(color_map.values())
        return len(chr_nbr)
    def dot(self, arg):
        colors_dots = {
            0:'\033[91m%s\033[0m'%'●',
            1:'\033[92m%s\033[0m'%'●',
            2:'\033[93m%s\033[0m'%'●',
            3:'\033[94m%s\033[0m'%'●',
            4:'\033[95m%s\033[0m'%'●',
            5:'\033[96m%s\033[0m'%'●'
        }
        return colors_dots[arg]

    def display(self):
        color_map = self.color_nodes()
        nodes = sorted(list(color_map.keys()), key=lambda x: color_map[x])
        myMap = {}
        for i in nodes:
            myMap[i] = color_map[i]
        chr_nbr = self.chromatic_number()
        dbar = '────'*len(color_map.keys())
        print ('\t\t\033[93m%s\033[0m%d'%("NOMBRE CHROMATIQUE:",chr_nbr))
        print('	   ',"┌─%s─┐"%(dbar))
        print('            │  ',end='')
        for vertix in nodes:
            print (vertix,end='   ')
        print("│")
        print('            ├',end='')
        print("%s──┤"%dbar)
        print('            │  ',end='')
        for color in myMap.values():
            print (self.dot(color),end='   ')
        print("│")
        print('	   ',"└─%s─┘"%(dbar))
        print ('\n\n')
def main():
    myGraph = {
        1:[2,3,6],
        2:[1,3,5,6],
        3:[1,2,4,5],
        4:[3,5,6],
        5:[4,3,2],
        6:[4,3,2,1]
    }
#    myGraph = {
#        1:[6,7,8],
#        2:[5,7,8],
#        3:[8,6,5],
#        4:[7,6,5],
#        5:[2,3,4],
#        6:[1,3,4],
#        7:[1,2,4],
#        8:[1,2,3]
#    }
#    myGraph = {
#        1:[2,3,4,5,6,7,8],
#        2:[1,3,4,6,5,7,8],
#        3:[1,2,4,7,8,6,5],
#        4:[1,2,3,8,7,6,5],
#        5:[1,6,7,2,3,4],
#        6:[2,5,7,8,1,3,4],
#        7:[1,2,4],
#        8:[1,2,3]
#    }
    obj = Welsh_Powell(myGraph)
    print ('\n')
    print ("""
	   ┌─────────────────────────────┐
	   │   COLORATION:WELSH_POWELL   │
	   └─────────────────────────────┘
	""")
    obj.display()
if __name__ == '__main__':
    main()
