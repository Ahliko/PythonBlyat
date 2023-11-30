from class_character import Character
import random

class Aberration(Character):
    def competence(self, target : list):
        random.seed()
        charach_to_att = random.randint(0, len(target)-1)
        boost = int(self.atk + (self.atk * (20/100)))
        old_atk = self.atk
        self.atk = boost
        self.attack(target[charach_to_att])
        self.atk = old_atk

    def choice(self, lst : list):
        ch = random.randint(0, 100)
        charach_to_att = random.randint(0, len(lst)-1)
        if ch < 80:
            self.attack(lst[charach_to_att])
        else:
            self.competence(lst)