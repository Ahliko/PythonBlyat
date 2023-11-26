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
        self.ult_pts += 30
        if self.ult_pts > self.max_ult_pts:  # TODO: Fix this (add a property max_ult_pts)
            self.ult_pts = self.max_ult_pts

    def ultimate(self, target: Character) -> bool:
        if self.ult_pts == self.max_ult_pts:
            old_atk = self.atk
            self.atk = (self.atk * (240 / 100))
            self.attack(target)
            self.atk = old_atk
            self.ult_pts = 0
        else:
            return False
