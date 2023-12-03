from class_character import Character


class Hunt(Character):

    def __init__(self, _id: int, name: str, critrate: int, critdmg: int):
        super().__init__(_id, name, critrate, critdmg)
        self.maxhp = 650
        self.hp = self.maxhp
        self.atk = 325
        self._def = 15
        self.maxultpts = 110
        self.speed = 14

    def ability(self, target: Character, game):
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        old_atk = self.atk
        old_critrate = self.critrate
        old_critdmg = self.critdmg
        self.atk += (self.atk * (15 / 100))
        self.critrate += 30
        self.critdmg += self.critdmg * (20 / 100)
        self.attack(target, game)
        self.atk = old_atk
        self.critdmg = old_critdmg
        self.critrate = old_critrate
        self.add_ultpts(30)
        self.cooldown = 2
        if self.ultpts > self.maxultpts:
            self.ultpts = self.maxultpts
        self.turn = False

    def ultime(self, target: Character, game) -> bool:
        if self.ultpts == self.maxultpts:
            print(f"{self.name} utlise son ultime !")
            old_atk = self.atk
            self.atk = (self.atk * (240 / 100))
            self.attack(target, game)
            self.atk = old_atk
            self.ultpts = 0
            self.turn = False
        else:
            print("Vous n'avez pas assez de points d'ultime")
