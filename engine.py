from __future__ import annotations
from class_character import Character


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
            if charac.turn:
                occ += 1
        if occ == len(lst):
            self.__turng += 1
            for charac in lst:
                charac.turn = True
        else:
            self.next_character(lst)

    @property
    def turng(self):
        return self.__turng

    @turng.setter
    def turng(self, amount):
        self.__turng = amount


Lelfe = Character("CC", 100, 10, 122)
Lelfe.turn = False
Nain = Character("GH", 100, 122, 1)
Nain.turn = False
engine = Engine()
print(engine.next_character([Lelfe, Nain]))
