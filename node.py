from ant import Ant, Team
from colours import Colours


class Node:
    def __init__(self, team: Team):
        self.__ants_map = {}
        self.colour = Colours.WHITE
        self.owning_team = team

    def add_new_ant(self, ant: Ant):
        if ant.team not in self.__ants_map:
            self.__ants_map[ant.team]([ant])
        else:
            self.__ants_map[ant.team].append(ant)

    def remove_ant(self, ant: Ant):
        res = self.__ants_map[ant.team]
        if not res:
            return
        
        res.remove(ant)

    def trigger_attack(self):
        dmg_map = {}  # Stores the total damage to the ants by team at node
        for ant in self.__ants_map:
            if ant.owning_team not in dmg_map:
                dmg_map[ant.owning_team] = ant.attackStrength
            else:
                dmg_map[ant.owning_team] += ant.attackStrength
        if len(dmg_map.keys()) <= 1:
            return

        hp_map = {} # Stores the total health of the ants by team at node
        for ant in self.__ants_map:
            if ant.owning_team not in hp_map:
                hp_map[ant.owning_team] = ant.health
            else:
                hp_map[ant.owning_team] += ant.health

        dmg_max = (Team.NONE, -1)  # damage, team map
        for key in dmg_map.keys():
            dmg_max = (key, key, max(dmg_map[key], dmg_max[0]))

        draw = False
        for key in dmg_map.keys():
            if key == dmg_max[0]:
                continue
            else:
                if dmg_max[1] > hp_map[key]:
                    self.__ants_map[key].clear()
                    draw = True
        if not draw:
            self.colour = Colours.BLUE if dmg_max[0] == Team.BLUE else Colours.RED

        
    def update(self):
        self.trigger_attack()

        

