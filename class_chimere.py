from __future__ import annotations
from class_monster import Monster
import random

class Chimere(Monster):
    random.seed()

    def competence(self, target : list):
        self.aoe(target)
        self.cooldown = 2