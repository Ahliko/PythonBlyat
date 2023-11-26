from __future__ import annotations
import random


class Character:
    def __init__(self, name: str, max_health: int, atk: int, _def: int) -> None:
        self.__name: str = name
        self.__maxhp: int = max_health
        self.__hp: int = max_health
        self.__atk: int = atk
        self.__def: int = _def
        self.__shield: int = 0  # shield
        self.__critdmg: int = 50  # dégats crit %
        self.__critrate: int = 5  # chances de coup crit
        self.__ultime: int = 0  # points d'ultime
        self.__turn: bool = True  # s'il peut jouer ou non
        self.__speed: int = 0
        random.seed()

    def __str__(self) -> str:
        return (f"name : {self.__name}, HPMAX : {self.__maxhp}, HP {self.__hp}, ATK : {self.__atk}, DEF : {self.__def},"
                f" TC : {self.__critrate}, DC : {self.__critdmg}")

    def is_alive(self) -> bool:
        if self.__hp <= 0:
            self.__turn = False
            return False
        else:
            return True

    def compute_damages(self) -> int | float:
        if random.randint(0, 100) <= self.__critrate:
            return self.__atk + (self.__atk * (self.__critdmg / 100))
        else:
            return self.__atk

    def compute_wounds(self, damages: int) -> int:
        return damages - self.__def

    def attack(self, target: Character) -> None:
        if not self.is_alive():
            return
        self.__ultime += 15
        damages = int(self.compute_damages())
        print(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {self.__atk})")
        self.__turn = False
        target.defense(damages)

    def defense(self, damages: int) -> None:
        wounds = self.compute_wounds(damages)
        print(f"🛡️ {self.__name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self.__def})")
        self.decrease_health(wounds)

    def decrease_health(self, amount: int) -> None:
        self.__hp -= amount

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, amount: int) -> None:
        self.__hp = amount

    @property
    def maxhp(self) -> int:
        return self.__maxhp

    @maxhp.setter
    def maxhp(self, amount: int) -> None:
        self.__maxhp = amount

    @property
    def atk(self) -> int:
        return self.__atk

    @atk.setter
    def atk(self, amount: int) -> None:
        self.__atk = amount

    @property
    def _def(self) -> int:
        return self.__def

    @_def.setter
    def _def(self, amount: int) -> None:
        self.__def = amount

    @property
    def shield(self) -> int:
        return self.__shield

    @shield.setter
    def shield(self, amount: int) -> None:
        self.__shield = amount

    @property
    def critdmg(self) -> int:
        return self.__critdmg

    @critdmg.setter
    def critdmg(self, amount: int) -> None:
        self.__critdmg = amount

    @property
    def critrate(self) -> int:
        return self.__critrate

    @critrate.setter
    def critrate(self, amount: int) -> None:
        self.__critrate = amount

    @property
    def name(self) -> str:
        return self.__name

    @property
    def turn(self) -> bool:
        return self.__turn

    @turn.setter
    def turn(self, boolean: bool) -> None:
        self.__turn = boolean

    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, amount: int) -> None:
        self.__speed = amount

    @property
    def ultime(self) -> int:
        return self.__ultime

    @ultime.setter
    def ultime(self, amount: int) -> None:
        self.__ultime = amount
