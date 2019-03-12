from business.algorithm import Algorithm
from business.node import Node


def find_node(list_nodes, kind):
    for node in list_nodes:
        if node.get_kind() == kind:
            return node
    raise ValueError('Nodo: ({}) no encontrado '.format(kind))


def clear_nodes(list_nodes):
    for node in list_nodes:
        node.parent = None
    return list_nodes


def run(matrix_coord):
    list_nodes = []
    required_nodes = []
    for i in range(len(matrix_coord)):
        for j in range(len(matrix_coord[i])):
            node = Node(x=i, y=j, kind=matrix_coord[i][j])
            list_nodes.append(node)
            if matrix_coord[i][j] == 'o':
                required_nodes.append(node)

    algorithm = Algorithm(list_nodes)
    i_node = find_node(list_nodes, 'i')
    way = [(i_node.get_x(), i_node.get_y())]
    for required in required_nodes:
        way += algorithm.run(i_node, required)
        i_node = required
        clear_nodes(list_nodes)
    f_node = find_node(list_nodes, 'f')
    way += algorithm.run(i_node, f_node)
    print('Camino Encontrado:')
    print(", ".join(["({},{})".format(item[0], item[1]) for item in way]))
    return way

