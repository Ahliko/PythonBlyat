from __future__ import annotations
from class_monster import Monster
import random

class Chimere(Monster):
    random.seed()
    def __init__(self, _id: int, name : str, critrate : int, critdmg : int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 600
        self.hp = self.maxhp
        self.atk = 90
        self._def = 15
        self.speed = 13

    def ability(self, target : list):
        self.turn = False
        self.aoe(target)
        self.cooldown = 2