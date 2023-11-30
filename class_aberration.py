from class_monster import Monster
import random

class Aberration(Monster):
    def competence(self, target : list):
        random.seed()
        charach_to_att = random.randint(0, len(target)-1)
        boost = int(self.atk + (self.atk * (20/100)))
        old_atk = self.atk
        self.atk = boost
        self.attack(target[charach_to_att])
        self.atk = old_atk
        self.cooldown = 2