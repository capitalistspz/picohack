from ant import Ant, AntType, Team
from colours import Colours

class Player:
    def __init__(self, player_no: int, team: Team):
        self.__player_no = player_no
        self.owned_ants: list[Ant] = list()
        self.action_points = 3
        self.max_action_points = 3
        self.selected_actions_count = 0
        self.colour = Colours.BLUE if team == team.BLUE else Colours.RED
        self.team = team

    def add_random_ant(self):
        ant = Ant(ant_type=AntType.WORKER, team=self.team)
        ant.randomize_attributes()
        self.owned_ants.append(ant)


