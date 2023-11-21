from class_character import Character

class Hunt(Character):
    def ability(self, who: Character):
        old_atk = self._atk
        old_critrate = self._critrate
        old_critdmg = self._critdmg
        self._atk += int((self._atk * (15 / 100)))
        self._critrate += 30
        self._critdmg += int(self._critdmg * (20 / 100))
        print(f"old : {old_atk}, current : {self._atk}ATK, CRIT DMG : {self._critdmg}%, CRIT RATE : {self._critrate}%")
        self.attack(who)
        self._atk = old_atk
        self._critdmg = old_critdmg
        self._critrate = old_critrate
        print(f"here : {self._atk}")