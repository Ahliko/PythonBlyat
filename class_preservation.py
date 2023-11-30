from class_character import Character


class Preservation(Character):

    def __init__(self, name: str, critrate: int, critdmg: int):
        super().__init__(name, critrate, critdmg)
        self.maxhp = 900
        self.hp = self.maxhp
        self.atk = 30
        self._def = 60
        self.maxultpts = 130
        self.speed = 9

    def ability(self, target: Character):
        target.shield = int(target.shield + (target.maxhp * (15 / 100)))
        self.ultime += 20
        return self.shield

    def use_ultime(self, target: list):
        if self.ultime == self.max_ult_pts:
            for i in target:
                i.shield = int(i.shield + (i._def * (40 / 100) + 20))
        else:
            print("Vous n'avez pas assez de points d'ultime")
            return
        self.ultime = 0
