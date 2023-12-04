from __future__ import annotations
from classes.monsters.class_monster import Monster
import random

class Chimere(Monster):
    random.seed()
    def __init__(self, _id: int, name : str, critrate : int, critdmg : int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 600
        self.hp = self.maxhp
        self.atk = 120
        self._def = 15
        self.speed = 13

    def ability(self, target : list, game):
        self.turn = False
        print(f"{self.name} utilise sa compétence spéciale : Chimère")
        game.history.append(f"{self.name} utilise sa compétence spéciale : Chimère")
        print(f"{self.name} attaque tout le monde")
        game.history.append(f"{self.name} attaque tout le monde")
        self.aoe(target, game)
        self.cooldown = 2