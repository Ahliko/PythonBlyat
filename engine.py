from __future__ import annotations
from class_character import Character
import random

class Engine:
    def __init__(self) -> None:
        self.__turng: int = 1

    def next_character(self, lst: list):
        for charac in lst:
            if charac.turn:
                return charac.name
        self.next_turn(lst)

    def next_turn(self, lst: list):
        occ = 0
        for charac in lst:
            if charac.turn == False:
                occ += 1
        if occ == len(lst):
            self.__turng += 1
            for charac in lst:
                charac.turn = True
            self.next_character(lst)
        else:
            self.next_character(lst)

    def random_monster(self):
        ennemis = []
        nb = 1
        for i in range(3):
            random.seed()
            rd = random.randint(1, 3)
            match rd:
                case 1:
                    ab = Character("aberration" + str(nb), 100, 3, 3)
                    ennemis.append(ab)
                case 2:
                    ch = Character("chimere" + str(nb), 100, 4, 5)
                    ennemis.append(ch)
                case 3:
                    print("cc")
        return ennemis

    @property
    def turng(self):
        return self.__turng

    @turng.setter
    def turng(self, amount):
        self.__turng = amount

engine = Engine()
lst = engine.random_monster()
print(lst[0])