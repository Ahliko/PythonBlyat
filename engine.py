from __future__ import annotations
from class_aberration import Aberration
from class_chimere import Chimere
from class_golem import Golem
from class_hunt import Hunt
import random
from game import Game


class Engine:
    def __init__(self, game: Game) -> None:
        self.__turng: int = 1
        self.__game = game

    @staticmethod
    def sort_speed(lst: list) -> list:
        sorted_list = sorted(lst, key=lambda x: x.speed)
        sorted_list.reverse()
        return sorted_list

    def next_character(self, lst: list):
        for charac in lst:
            if charac.turn:
                return charac.name
        self.next_turn(lst)

    def next_turn(self, lst: list):
        occ = 0
        for charac in lst:
            if not charac.turn:
                occ += 1
        if occ == len(lst):
            for charac in lst:
                charac.turn = True
                self.competence_cooldown(lst)
            self.turng += 1
            self.next_character(lst)
        else:
            self.next_character(lst)

    @staticmethod
    def competence_cooldown(lst: list):
        for charac in lst:
            if charac.cooldown > 0:
                charac.cooldown -= 1

    def random_monster(self):
        nb = 1
        for i in range(3):
            random.seed()
            rd = random.randint(1, 3)
            match rd:
                case 1:
                    self.__game.monsters.append(Aberration("aberration" + str(nb), 5, 10))
                case 2:
                    self.__game.monsters.append(Chimere("chimere" + str(nb), 5, 10))
                case 3:
                    self.__game.monsters.append(Golem("golem" + str(nb), 5, 10))

    @property
    def turng(self):
        return self.__turng

    @turng.setter
    def turng(self, amount):
        self.__turng = amount
