from __future__ import annotations
from classes.monsters.class_aberration import Aberration
from classes.monsters.class_chimere import Chimere
from classes.monsters.class_golem import Golem
import random
from game import Game


class Engine:
    def __init__(self, game: Game) -> None:
        self.__turng: int = 1
        self.__game = game

    @staticmethod
    def sort_speed(lst: list) -> list:
        sorted_list = sorted(lst, key=lambda x: x.speed)
        return sorted_list

    @staticmethod
    def next_character(lst: list):
        for charac in lst:
            if charac.turn and charac.is_alive():
                return charac.id

    def next_turn(self, lst: list):
        self.__game.history = []
        self.__game.history.append(f"Turn {self.turng}")
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
        id = 4
        self.__game.monsters = []
        for i in range(3):
            random.seed()
            rd = random.randint(1, 3)
            match rd:
                case 1:
                    self.__game.monsters.append(Aberration(id, "aberration" + f" {str(nb)}", 5, 10))
                    nb += 1
                    id += 1
                case 2:
                    self.__game.monsters.append(Chimere(id, "chimere" + f" {str(nb)}", 5, 10))
                    nb += 1
                    id += 1
                case 3:
                    self.__game.monsters.append(Golem(id, "golem" + f" {str(nb)}", 5, 10))
                    nb += 1
                    id += 1

    def final_list(self):
        self.__game.all_characters = []
        self.random_monster()
        for key, charac in self.__game.characters.items():
            charac.turn = True
            charac.hp = charac.maxhp
            self.__game.all_characters.append(charac)
        for charac in self.__game.monsters:
            self.__game.all_characters.append(charac)
        self.__game.all_characters = self.sort_speed(self.__game.all_characters)
        for i in self.__game.all_characters:
            print(i.__str__() + "\n")

    @staticmethod
    def is_win(lst: list):
        occ = 0
        for charac in lst:
            if not charac.is_alive():
                occ += 1
        if occ == len(lst):
            return True
        else:
            return False

    @property
    def turng(self):
        return self.__turng

    @turng.setter
    def turng(self, amount):
        self.__turng = amount

    @staticmethod
    def reset_cooldown(all_characters):
        for charac in all_characters:
            if charac.cooldown > 0:
                charac.cooldown = 0

    @staticmethod
    def reset_buf(param):
        for charac in param:
            charac.buf["remaining"] = 0
