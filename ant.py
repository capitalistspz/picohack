import random
from enum import Enum


class AntType(Enum):
    WORKER = 0,
    QUEEN = 1


class Team(Enum):
    RED = 0,
    BLUE = 1


class AntAbility:
    def __init__(self, damage, ab_range, friendly_fire=False):
        self.__damage = damage
        self.__range = ab_range
        self.__friendly_fire = friendly_fire


antTypes = ["worker", "queen"]
teams = ["red ant", "black ant"]


class Ant:
    ant_type = ""
    team = ""
    level = 0
    health = 0
    attackStrength = 0
    ability = ""

    def __int__(self, ant_type, team, level, health, attack_strength, ability):
        self.ant_type = ant_type
        self.team = team
        self.level = level
        self.health = health
        self.attackStrength = attack_strength
        self.ability = ability

    def __init__(self, ant_type, team):
        self.ant_type = ant_type
        self.team = team
        self.level = 1
        self.health = 1
        self.attackStrength = 1
        self.ability = "none"

    def randomize_attributes(self):
        self.health = random.randint(1, 20)
        self.attackStrength = random.randint(1, 15)



class Army(Ant):
    pass
