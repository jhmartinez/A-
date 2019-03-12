import math


class Node(object):

    def __init__(self, x=None, y=None, parent=None, kind=None):
        self.parent = parent
        self._x = x
        self._y = y
        self._kind = kind

    def get_f(self, f_node):
        g = self.get_g(self.parent)
        h = self.get_h(f_node)
        return g + h

    def get_g(self, dad):
        if dad is not None:
            if self._x == dad.get_x() or self._y == dad.get_y():
                if self._kind == 'p':
                    return 2 + dad.get_g(dad.parent)
                else:
                    return 1 + dad.get_g(dad.parent)
            else:
                if self._kind == 'p':
                    return math.sqrt(2) + dad.get_g(dad.parent) + 1
                else:
                    return math.sqrt(2) + dad.get_g(dad.parent)
        else:
            return 0

    def get_h(self, f_node):
        return math.sqrt((self._x - f_node.get_x())**2 + (self._y - f_node.get_y())**2)

    def get_kind(self):
        return self._kind

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __str__(self):
        return "X({})-Y({})-PARENT({})".format(self._x, self._y, self.parent)
