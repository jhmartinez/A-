# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals

import os
import sys
from threading import Thread

import pygame
from pygame.locals import *
import pygame.font

from business.api import run as run_business

CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SPRITES_PATH = os.path.join(BASE_PATH, 'sprites')
SOUNDS_PATH = os.path.join(BASE_PATH, 'sounds')


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.rect = pos[0] - CELL_SIZE, pos[1] - CELL_SIZE

    def update(self, pos):
        pass


class Start(Sprite):
    def __init__(self, pos):
        super(Start, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'start.png'))


class Player(Sprite):
    def __init__(self, pos):
        super(Player, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'player.png'))

    def update(self, pos):
        if pos:
            self.rect = pos[0] - CELL_SIZE, pos[1] - CELL_SIZE


class Runway(Sprite):

    def __init__(self, pos):
        super(Runway, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'runway.png'))


class Finish(Sprite):

    def __init__(self, pos):
        super(Finish, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'finish.png'))


class Barrier(Sprite):

    def __init__(self, pos):
        super(Barrier, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'barrer.png'))


class Dangerous(Sprite):

    def __init__(self, pos):
        super(Dangerous, self).__init__(pos)
        self.image = pygame.image.load(os.path.join(SPRITES_PATH, 'danger.png'))


def load_map(matrix_coord):
    dimensions = len(matrix_coord), len(matrix_coord[0])
    total_width = CELL_SIZE * dimensions[1]
    total_height = CELL_SIZE * dimensions[0]
    sprites = pygame.sprite.Group()
    i_is_found = False
    f_is_found = False
    for x, items in enumerate(matrix_coord, 1):
        for y, item in enumerate(items, 1):
            cls = None
            player = None
            if item == 'i' and not i_is_found:
                cls = Start
                player = Player
                i_is_found = True
            elif item == 'f' and not f_is_found:
                cls = Finish
                f_is_found = True
            elif item == 'p':
                cls = Dangerous
            elif item == 'o':
                cls = Runway
            elif item == 'x':
                cls = Barrier
            if cls:
                pos = (y * CELL_SIZE, x * CELL_SIZE)
                sprites.add(cls(pos))
                if player:
                    sprites.add(player(pos))
    return sprites, (total_width, total_height)


def paint_map(screen, size, matrix_coord):
    for i in range(1, len(matrix_coord)):
        x0, x1 = 0, size[0]
        y0, y1 = i * CELL_SIZE, i * CELL_SIZE
        pygame.draw.line(screen, BLACK, [x0, y0], [x1, y1], 1)
        for j in range(1, len(matrix_coord[i])):
            x0, x1 = j * CELL_SIZE, j * CELL_SIZE
            y0, y1 = 0, size[1]
            pygame.draw.line(screen, BLACK, [x0, y0], [x1, y1], 1)


def execute(matrix, data):
    print('EJECUTANDO ALGORITMO')
    try:
        data['way'] = run_business(matrix)
    except ValueError as e:
        data['error'] = e.args[0]
    except Exception:
        data['error'] = 'Ha ocurrido un error inesperado'


def run(matrix_coord):
    pygame.init()
    sprites, size = load_map(matrix_coord)
    screen = pygame.display.set_mode((size[0], size[1]))
    pygame.display.set_caption("Laberinto")

    data = {'way': [], 'error': ''}
    clock = pygame.time.Clock()
    pos = 0

    font = pygame.font.SysFont('Comic Sans MS', 25)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key in (K_DOWN, K_RIGHT) and pos < len(data['way']):
                pygame.mixer.music.load(os.path.join(SOUNDS_PATH, '2.wav'))
                pygame.mixer.music.play(0)
                pos += 1
                if pos == len(data['way']) - 1:
                    pygame.mixer.music.load(os.path.join(SOUNDS_PATH, '3.mp3'))
                    pygame.mixer.music.play(0)
            elif event.type == KEYDOWN and event.key in (K_UP, K_LEFT) and pos > 0:
                pygame.mixer.music.load(os.path.join(SOUNDS_PATH, '2.wav'))
                pygame.mixer.music.play(0)
                pos -= 1
            elif event.type == KEYDOWN and event.key == K_SPACE and not data['error']:
                thread = Thread(target=execute, args=(matrix_coord, data))
                thread.start()

        screen.fill(WHITE)
        paint_map(screen, size, matrix_coord)
        sprites.draw(screen)

        if data['error']:
            error = font.render(data['error'], True, BLACK)
            screen.blit(error, (0, size[1] / 2 - 25))
        elif 0 <= pos < len(data['way']):
            coor = data['way'][pos]
            x, y = (coor[1] + 1) * CELL_SIZE, (coor[0] + 1) * CELL_SIZE
            sprites.update((x, y))

        # Actualizamos la pantalla
        pygame.display.flip()

        # Pausa
        clock.tick(100)

    return 0
