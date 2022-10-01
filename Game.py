import math
from typing import Union
from enum import Enum
import pygame.display
from pygame.surface import SurfaceType, Surface

from ant import Team
from colours import Colours
from node import Node
from player import Player


class GameState(Enum):
    NONE = 0
    CHOOSING_ACTION = 1


class Game:
    def __init__(self, size):
        self.__screen = pygame.display.set_mode((size, size))
        self.__size = size
        self.__current_player = 0
        self.__player_list: list[Player] = list()
        self.__displayable_surfaces = list()

        self.__popup = None

        self.__grid = []

        self.__state = GameState.NONE

        for i in range(0, 5):
            col = []
            for j in range(0, 5):
                col.append(Node(team=Team.NONE))
            self.__grid.append(col)
        node_a = Node(Team.RED)
        node_a.colour = Colours.RED

        node_b = Node(Team.BLUE)
        node_b.colour = Colours.BLUE
        self.__player_list.append(Player(0, Team.BLUE))
        self.__player_list.append(Player(1, Team.RED))

        self.__grid[0][4] = node_a
        self.__grid[4][0] = node_b

    def node_at_pos(self, x, y) -> Node:
        x_val = x / 120
        y_val = y / 120

        if 0 <= x > self.__size or 0 <= y > self.__size:
            print(f"Pos out of bounds: ({x}, {y})")
            return None

        grid_x = int(math.floor(x_val))
        grid_y = int(math.floor(y_val))

        print(f"Grid X: {grid_x}, Grid Y: {grid_y}")

        return self.__grid[grid_x][grid_y]

    def choose_action(self, node: Node, chosen_action) -> bool:
        player = self.__player_list[self.__current_player]

        if player.action_points <= 0:
            print(f"No action points remaining, switching player")
            self.switch_player()
            return False
        if self.__popup is None:
            self.display_choose_opt_dialogue(pygame.mouse.get_pos())
            return False

        if chosen_action == 1:
            if len(player.owned_ants) < 1:
                print("No ants remaining, choose a different action")
            else:
                node.add_new_ant(player.owned_ants.pop())

        elif chosen_action == 2:
            player.add_random_ant()
            player.action_points -= 1
        else:
            return False
        self.__popup = None
        return True
    def display_choose_opt_dialogue(self, pos: tuple[int, int]):
        font = pygame.font.Font(None, 24)
        img = font.render('1: Use one ant for attack, 2: Create new ant', True, Colours.BLACK)
        self.__popup = (img, pos)

    def update_nodes(self):
        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                self.__grid[i][j].update()
    def draw(self):
        self.__screen.fill(Colours.WHITE)

        for i in range(len(self.__grid)):
            for j in range(len(self.__grid[0])):
                val = self.__grid[i][j]
                draw_col = val.colour
                width = 60

                if val.colour == Colours.WHITE:
                    draw_col = Colours.BLACK
                    width = 2

                pygame.draw.circle(self.__screen, draw_col, (60 + (i * 120), 60 + (j * 120)),
                                   50, width)

        if self.__popup is not None:
            self.__screen.blit(self.__popup[0], self.__popup[1])

        pygame.display.flip()

    def switch_player(self):
        self.__current_player = (self.__current_player + 1) % len(self.__player_list)
