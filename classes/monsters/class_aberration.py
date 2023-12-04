from classes.monsters.class_monster import Monster
import random

from lib.game import Game


class Aberration(Monster):
    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 750
        self.hp = self.maxhp
        self.atk = 150
        self._def = 30
        self.speed = 12

    def ability(self, target: list, game: Game):
        random.seed()
        charach_to_att = random.randint(0, len(target) - 1)
        boost = int(self.atk + (self.atk * (20 / 100)))
        old_atk = self.atk
        self.atk = boost
        print(f"{self.name} utilise sa compétence spéciale : Aberration")
        game.history.append(f"{self.name} utilise sa compétence spéciale : Aberration")
        print(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
        game.history.append(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
        self.attack(target[charach_to_att], game)
        self.atk = old_atk
        self.turn = False
        self.cooldown = 2
