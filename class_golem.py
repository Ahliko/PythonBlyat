from class_character import Character
import random

class Golem(Character):

    def competence(self):
        self.shield = self.defense +(self.defense * (45 / 100))
        self.turn = False

    def choice(self, lst : list):
        ch = random.randint(0, 100)
        charach_to_att = random.randint(0, len(lst)-1)
        if ch < 80:
            self.attack(lst[charach_to_att])
        else:
            self.competence()