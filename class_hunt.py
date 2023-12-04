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
        self.buf = {
            "id": 0,
            "ability": False,
            "atk": self.atk,
            "critrate": self.critrate,
            "critdmg": self.critdmg,
            "remaining": 0
        }

    def ability(self, target: Character, game):
        if self.cooldown > 0:
            print("Vous ne pouvez pas utiliser cette compétence pour le moment")
            game.history.append("Vous ne pouvez pas utiliser cette compétence pour le moment")
            return self.cooldown
        old_atk = self.atk
        print(f"{self.name} utilise sa compétence spéciale ! : Balle de Plomb")
        game.history.append(f"{self.name} utilise sa compétence spéciale ! : Balle de Plomb")
        old_critrate = self.critrate
        old_critdmg = self.critdmg
        self.atk += (self.atk * (15 / 100))
        self.critrate += 30
        self.critdmg += self.critdmg * (20 / 100)
        print(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
        game.history.append(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
        print(f"Le taux de critique de {self.name} est passé de {old_critrate} à {self.critrate} pour ce tour")
        game.history.append(
            f"Le taux de critique de {self.name} est passé de {old_critrate} à {self.critrate} pour ce tour")
        print(f"Les dégâts de critiques de {self.name} sont passés de {old_critdmg} à {self.critdmg} pour ce tour")
        game.history.append(
            f"Les dégâts de critiques de {self.name} sont passés de {old_critdmg} à {self.critdmg} pour ce tour")
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
            print(f"{self.name} utlise son ultime ! : Lacération")
            game.history.append(f"{self.name} utlise son ultime ! : Lacération")
            old_atk = self.atk
            self.atk = (self.atk * (190 / 100))
            print(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
            game.history.append(f"L'attaque de {self.name} est passé de {old_atk} à {self.atk} pour ce tour")
            self.attack(target, game)
            self.atk = old_atk
            self.ultpts = 0
            self.turn = False
        else:
            print("Vous n'avez pas assez de points d'ultime")
            game.history.append("Vous n'avez pas assez de points d'ultime")
