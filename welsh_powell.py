#!/usr/bin/env python
# TODO: make similar color mapping close together
# TODO: make the code more readble
class Welsh_Powell:
    def __init__(self,Graph_init):
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
        chr_nbr = self.chromatic_number()
        dbar = '────'*len(color_map.keys())
        print ()
        print ('\t\t\033[93m%s\033[0m%d'%("NOMBRE CHROMATIQUE:",chr_nbr))
        print('	   ',"┌─%s─┐"%(dbar))
        print('            │  ',end='')
        for vertix in color_map.keys():
            print (vertix,end='   ')
        print("│")
        print('            ├',end='')
        print("%s──┤"%dbar)
        print('            │  ',end='')
        for color in color_map.values():
            print (self.dot(color),end='   ')
        print("│")
        print('	   ',"└─%s─┘"%(dbar))
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
    obj = Welsh_Powell(myGraph)
    print ("""
	   ┌─────────────────────────────┐
	   │   COLORATION:WELSH_POWELL   │
	   └─────────────────────────────┘
	""")
    obj.display()
if __name__ == '__main__':
    main()
