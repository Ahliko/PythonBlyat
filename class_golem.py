from class_monster import Monster
import random


class Golem(Monster):
    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 900
        self.hp = self.maxhp
        self.atk = 30
        self._def = 55
        self.speed = 8

    def ability(self, target: list):
        self.shield = self._def + (self._def * (45 / 100))
        self.turn = False
        self.cooldown = 2
