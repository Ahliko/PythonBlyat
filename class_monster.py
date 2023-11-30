from class_character import Character
import random

class Monster(Character):
    def choice(self, lst : list):
        ch = random.randint(0, 100)
        charach_to_att = random.randint(0, len(lst)-1)
        if ch < 80:
            self.attack(lst[charach_to_att])
        else:
            if self.cooldown > 0:
                self.attack(lst[charach_to_att])
            else:
                self.competence(lst)