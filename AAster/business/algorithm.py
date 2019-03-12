
class Algorithm(object):
    def __init__(self, list_nodes):
        self._list_nodes = list_nodes

    def run(self, i_node, f_node):
        """Se ejecuta el algoritmo.
        :return: Camino encontrado
        """
        open_list = []
        closed_list = []
        open_list.append(i_node)
        while f_node not in closed_list and len(open_list) > 0:
            node_lesser_f = self.choose_node_lesser_f(open_list, f_node)
            closed_list.append(node_lesser_f)
            open_list.remove(node_lesser_f)
            neighbors_node = self.find_neighbors(node_lesser_f)
            for node in neighbors_node:
                if node not in open_list and not node.parent:
                    open_list.append(node)
                    node.parent = node_lesser_f
                elif node.get_g(node.parent) > node.get_g(node_lesser_f):
                    node.parent = node_lesser_f
        if not f_node.parent:
            raise ValueError('Nodo inaccesible')
        else:
            way = []
            aux = f_node
            while aux.parent:
                way.insert(0, aux)
                aux = aux.parent
            way = [(node.get_x(), node.get_y()) for node in way]
            return way

    def choose_node_lesser_f(self, open_list, f_node):
        """Se busca en la lista abierta el nodo con menor f.
        :param open_list: lista abierta
        :param f_node: nodo final
        :return:
        """
        node = open_list[0]
        for i in open_list:
            if i.get_f(f_node) < node.get_f(f_node):
                node = i
        return node

    def find_neighbors(self, node):
        """Se buscan los vecinos.
        :param node: Objeto de la clase 'Node'.
        :return: Lista de vecinos.
        """
        neighbors_list = []
        for e_node in self._list_nodes:
            added = False
            if node.get_x() == e_node.get_x() and node.get_y() - 1 == e_node.get_y():
                added = True
            elif node.get_x() == e_node.get_x() and node.get_y() + 1 == e_node.get_y():
                added = True
            elif node.get_x() + 1 == e_node.get_x() and node.get_y() == e_node.get_y():
                added = True
            elif node.get_x() - 1 == e_node.get_x() and node.get_y() == e_node.get_y():
                added = True
            elif node.get_x() + 1 == e_node.get_x() and node.get_y() + 1 == e_node.get_y():
                added = True
            elif node.get_x() - 1 == e_node.get_x() and node.get_y() + 1 == e_node.get_y():
                added = True
            elif node.get_x() - 1 == e_node.get_x() and node.get_y() - 1 == e_node.get_y():
                added = True
            elif node.get_x() + 1 == e_node.get_x() and node.get_y() - 1 == e_node.get_y():
                added = True
            if added and e_node.get_kind() != 'x':
                neighbors_list.append(e_node)
        for neighbor in neighbors_list:
            if neighbor == node.parent:
                neighbors_list.remove(neighbor)
        return neighbors_list
