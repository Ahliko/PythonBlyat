from __future__ import annotations
from class_character import Character

class Engine:

    def __init__(self) -> None:
        self.__turng : int = 1
    
    def next_character(list : []):
        for charac in list:
            if charac.turn == True:
                return charac.name
    
    def next_turn(self, list : []):
        occ = 0
        for charac in list:
            if charac.turn == False:
                occ += 1
        if occ == len(list):
            self.__turn += 1
            for charac in list:
                charac.turn = True
        else :
            self.next_perso(list)

    @property
    def turng(self):
        return self.__turng
    
    @turng.setter
    def turn(self, amount):
        self.__turng = amount


Lelfe = Character("CC", 100, 10, 122)
Lelfe.turn = False
Nain = Character("GH", 100, 122, 1)
print(Engine.next_character([Lelfe, Nain]))

