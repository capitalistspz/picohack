from ant import Ant
from colours import Colours


class Node:
    def __init__(self):
        self.__ants = list()
        self.colour = Colours.WHITE

    def add_new_ant(self, ant: Ant):
        self.__ants.append(ant)

    def remove_ant(self, ant: Ant):
        self.__ants.remove(ant)

    def trigger_attack(self):
        ant_map = {}
        for ant in self.__ants:
            if ant.team not in ant_map:
                ant_map[ant.team] = ant.attackStrength
            else:
                ant_map[ant.team] += ant.attackStrength


