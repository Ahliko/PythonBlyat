from class_character import Character


class Hunt(Character):

    def __init__(self, name: str, critrate: int, critdmg: int):
        super().__init__(name, critrate, critdmg)
        self.maxhp = 650
        self.hp = self.maxhp
        self.atk = 100
        self._def = 15
        self.maxultpts = 100
        self.speed = 14
        self.competence_need_turn = 2

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
        self.competence = False
        if self.ult_pts > self.max_ult_pts:
            self.ult_pts = self.max_ult_pts

    def ultimate(self, target: Character) -> bool:
        if self.ultpts == self.maxultpts:
            print(f"{self.name} utlise son ultime !")
            old_atk = self.atk
            self.atk = (self.atk * (240 / 100))
            self.attack(target)
            self.atk = old_atk
        else:
            print("Vous n'avez pas assez de points d'ultime")
            return
        self.ultpts = 0
