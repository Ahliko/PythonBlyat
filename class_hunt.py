from class_character import Character

class Hunt(Character):
    def ability(self, target: Character):
        old_atk = self.atk
        old_critrate = self.critrate
        old_critdmg = self.critdmg
        self.atk += (self.atk * (15 / 100))
        self.critrate += 30
        self.critdmg += self.critdmg * (20 / 100)
        self.attack(target)
        self.atk = old_atk
        self.critdmg = old_critdmg
        self.critrate = old_critrate

    def ultimate(self, target: Character):
        old_atk = self.atk
        self.atk = (self.atk * (240 / 100))
        self.attack(target)
        self.atk = old_atk