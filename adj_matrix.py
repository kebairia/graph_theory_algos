#!/bin/env python
#AUTHOR: Kebairia Zakaria
#EMAIL : z.kebairia@esi-sba.dz
#             _  _                     _        _
#    __ _  __| |(_)    _ __ ___   __ _| |_ _ __(_)_  __
#   / _` |/ _` || |   | '_ ` _ \ / _` | __| '__| \ \/ /
#  | (_| | (_| || |   | | | | | | (_| | |_| |  | |>  <
#   \__,_|\__,_|/ |___|_| |_| |_|\__,_|\__|_|  |_/_/\_\
#             |__/_____|
#
def creat_graph(length):
    graph = {}
    for i in range(length):
        print('Sommet: ',end='')
        sommet = input()
        print('Arcs: ',end='')
        arcs = input().split(',')
        graph[i] = arcs
    return graph
def graph2or_adj_matrix(myMtrix):
    for sommet in myMtrix.keys():
        print(sommet)
        
    

print('Enter the graph type[or/nr]: ',end='')
graph_type = input()
mygraph = creat_graph(6)
print(mygraph)
