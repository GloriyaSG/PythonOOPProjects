from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    DEFAULT_SUPPLY = ["Drink", "Food"]

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *players:[Player]):
        players_in = []
        for player in players:
            if player not in self.players:
                players_in.append(player.name)
                self.players.append(player)

        return f"Successfully added: {', '.join(players_in)}"

    def add_supply(self, *supply: [Supply]):
        [self.supplies.append(supp) for supp in supply]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in Controller.DEFAULT_SUPPLY:
            return

        for player in self.players:
            if player.name == player_name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        player.stamina = min(player.stamina + supply.energy, 100)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first = [p1 for p1 in self.players if p1.name == first_player_name][0]
        second = [p2 for p2 in self.players if p2.name == second_player_name][0]

        result = []
        if first.stamina == 0:
            result.append(f"Player {first_player_name} does not have enough stamina.")
        if second.stamina == 0:
            result.append(f"Player {second_player_name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        def curr_duel(smaller, greater):

            result = greater.stamina - smaller.stamina / 2

            if result <= 0:
                greater.stamina = 0
                return f"Winner: {smaller.name}"
            else:
                greater.stamina = result

            result2 = smaller.stamina - greater.stamina / 2
            if result2 <= 0:
                smaller.stamina = 0
                return f"Winner: {greater.name}"
            else:
                smaller.stamina = result2

            if first.stamina > second.stamina:
                return f"Winner: {first.name}"

            return f"Winner: {second.name}"

        if first.stamina < second.stamina:
            return curr_duel(first, second)

        elif first.stamina > second.stamina:
            return curr_duel(second, first)

    def next_day(self):
        for player in self.players:
            reducer = player.age * 2
            player.stamina = max(player.stamina - reducer, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
            +
            [s.details() for s in self.supplies]
        )