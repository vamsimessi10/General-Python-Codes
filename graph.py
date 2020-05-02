import numpy as np
import numpy as np
def matofnode(node,lst,num_nodes):
    l = [0 for i in range(num_nodes)]
    l[node] = 0
    for i in lst:
        if i[0] == node:
            for j in range(num_nodes):
                if j == i[1]:
                    l[i[1]] = 1
    return l

def graph_list2matrix(graph, num_nodes):
    """
    Arguments:
        graph   a list representation of the graph g where each entry
                 in the list is a tuple of (from,to) edges in the graph
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a numpy matrix where entries (i,j) represent edges from
        node i to node j
    """
    mat = []
    for i in range(num_nodes):
        mat.append(matofnode(i,graph,num_nodes))
    return np.matrix(mat)

graph_list2matrix([(0,1), (0,2), (0,3), (1,2),(2,1)], 4)

from collections import defaultdict
def graph_list2dict(graph, num_nodes):
    """
    Argumnents:
        graph     a list representation of the graph g where each entry
                  in the list is a tuple of (from,to) edges in the graph
        num_nodes  the number of nodes; each node will be labeled from
                   0 to num_nodes-1

    Returns:
        a dictionary where the key to each entry is the from
        node and the values are the edges to other nodes
    """
    d = defaultdict(list)
    for nodes in graph:
        d[nodes[0]].append(nodes[1])
    return dict(d)

graph = [(0,1), (0,2), (0,3), (1,2),(2,1)]

print (graph_list2dict(graph, 4))

def mat_2node(node,lst,num_nodes):
    l = []
    for i in range(num_nodes):
        if lst[i] == 1:
            l.append((node,i))
    return l
def graph_matrix2list(graph, num_nodes):
    """
    Arguments:
        graph   a numpy matrix where entries (i,j) represent edges from
                node i to node j

        num_nodes  the number of nodes; each node will be labeled from
                     0 to num_nodes-1

    Returns:
        a list representation of the graph g where each entry
        in the list is a tuple of (from,to) edges in the graph
    """
    list_final = []
    for i,j in zip(graph,range(num_nodes)):
        for k in mat_2node(j,i,num_nodes):
            list_final.append(k)
    return list_final

print (graph_matrix2list([ [0, 1, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0],], 4))

from collections import defaultdict
def mat_2node(node,lst,num_nodes):
    l = []
    for i in range(num_nodes):
        if lst[i] == 1:
            l.append((node,i))
    return l
def graph_matrix2dict(graph, num_nodes):
    """
    Arguments:
        graph   a numpy matrix where entries (i,j) represent edges from
                node i to node j
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a dictionary where the key to each entry is the from
        node and the values are the edges to other nodes
    """
    d = defaultdict(list)
    for i,j in zip(graph,range(num_nodes)):
        for k in mat_2node(j,i,num_nodes):
            d[k[0]].append(k[1])
    return dict(d)

print(graph_matrix2dict([ [0, 1, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0],], 4))


#Aum Sri Sairam
def graph_dict2list(graph, num_nodes):
    """
    Arguments:
        graph   a dictionary where the key to each entry is the from
                node and the values are the edges to other nodes
        num_nodes  the number of nodes; each node will be labeled from
                     0 to num_nodes-1

    Returns:
        a list representation of the graph g where each entry
        in the list is a tuple of (from,to) edges in the graph
    """
    l = []
    for from_node,to_nodeslst in graph.items():
        for to_node in to_nodeslst:
            l.append((from_node,to_node))
    return l 

graph = {0:[1,2,3,], 1:[2], 2:[1]}

print (graph_dict2list(graph, 4))

def matrofnode(node,dic,num_nodes):
    l = [0 for i in range(num_nodes)]
    l[node] = 0
    for key,value in dic.items():
        if key == node:
            for i in value:
                l[i] = 1
    return l
def graph_dict2matrix(graph, num_nodes):
    """
    Arguments:
        graph   a dictionary where the key to each entry is the from
                node and the values are the edges to other nodes
        num_nodes  the number of nodes; each node will be labeled from
                    0 to num_nodes-1

    Returns:
        a numpy matrix where entries (i,j) represent edges from
        node i to node j
    """
    mat = []
    for i in range(num_nodes):
        mat.append(matrofnode(i,graph,num_nodes))
    return np.matrix(mat)

graph = {0:[1,2,3,], 1:[2], 2:[1]}

graph_dict2matrix(graph,4)