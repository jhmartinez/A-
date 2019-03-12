# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from view.api import run as run_view
from business.api import run as run_business

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def run(mode):
    filename = os.path.join(BASE_PATH, 'source')
    if os.path.isfile(filename):
        matrix_coord = []
        with open(filename) as data:
            for line in data.readlines():
                words = [word.strip() for word in line.split(',') if word.strip() != '']
                matrix_coord.append(words)
        if mode == 'console':
            run_business(matrix_coord)
        else:
            run_view(matrix_coord)
    else:
        print('Fuente de datos no encontrada')


if __name__ == '__main__':
    if '-mode:console' in sys.argv:
        run('console')
    elif '-mode:window' in sys.argv:
        run('window')
    else:
        print("""
        Modo de ejecución incorrecta.
        Eliga:
        1. -mode:console
        2. -mode:window
        """)
