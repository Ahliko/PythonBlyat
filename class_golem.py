from class_monster import Monster
import random


class Golem(Monster):
    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 1325
        self.hp = self.maxhp
        self.atk = 220
        self._def = 55
        self.speed = 8

    def ability(self, target: list, game):
        print(f"{self.name} utilise sa compétence spéciale : Bouclier de pierre")
        self.shield = self._def + (self._def * (45 / 100))
        self.turn = False
        self.cooldown = 2
