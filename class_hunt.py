from class_character import Character

class Hunt(Character):
    def ability(self, who: Character):
        old_atk = self.atk
        old_critrate = self.critrate
        old_critdmg = self.critdmg
        self.atk += (self.atk * (15 / 100))
        self.critrate += 30
        self.critdmg += self.critdmg * (20 / 100)
        self.attack(who)
        self.atk = old_atk
        self.critdmg = old_critdmg
        self.critrate = old_critrate


perso = Hunt("Nom", 350, 200, 100)
perso.ability(perso)