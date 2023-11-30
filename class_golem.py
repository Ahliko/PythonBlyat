from class_monster import Monster
import random

class Golem(Monster):

    def competence(self):
        self.shield = self.defense +(self.defense * (45 / 100))
        self.turn = False
        self.cooldown = 2