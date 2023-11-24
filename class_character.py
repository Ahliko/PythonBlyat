from __future__ import annotations
import random

random.seed()

class Character:
    def __init__(self, name: str, max_health: int, atk: int, _def: int) -> None:
        self.__name = name
        self.__maxhp = max_health
        self.__hp = max_health
        self.__atk = atk
        self.__def = _def
        self.__shield = 0  # shield
        self.__critdmg = 50  # dégats crit %
        self.__critrate = 5  # chances de coup crit
        self.__ultime = 0 # points d'ultime
        self.__turn = True # si il peut jouer ou non
        self.__speed = 0

    def __str__(self):
        return (f"name : {self.__name}, HPMAX : {self.__maxhp}, HP {self.__hp}, ATK : {self.__atk}, DEF : {self.__def},"
                f" TC : {self.__critrate}, DC : {self.__critdmg}")

    def is_alive(self):
        if self.__hp <= 0:
            self.__turn = False
            return False
        else :
            return True

    def compute_damages(self):
        nb = random.randint(0, 100)
        if nb <= self.__critrate:
            return self.__atk + (self.__atk * (self.__critdmg / 100))
        else:
            return self.__atk

    def compute_wounds(self, damages):
        return damages - self.__def

    def attack(self, target: Character):
        self.__ultime += 15
        if not self.is_alive():
            return
        damages = int(self.compute_damages())
        print(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {self.__atk})")
        self.__turn = False
        target.defense(damages)

    def defense(self, damages):
        wounds = self.compute_wounds(damages)
        print(f"🛡️ {self.__name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self.__def})")
        self.decrease_health(wounds)

    def decrease_health(self, amount):
        self.__hp -= amount

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, amount):
        self.__hp = amount

    @property
    def maxhp(self):
        return self.__maxhp

    @maxhp.setter
    def maxhp(self, amount):
        self.__maxhp = amount

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, amount):
        self.__atk = amount

    @property
    def _def(self):
        return self.__def

    @_def.setter
    def _def(self, amount):
        self.__def = amount

    @property
    def shield(self):
        return self.__shield

    @shield.setter
    def shield(self, amount):
        self.__shield = amount

    @property
    def critdmg(self):
        return self.__critdmg

    @critdmg.setter
    def critdmg(self, amount):
        self.__critdmg = amount

    @property
    def critrate(self):
        return self.__critrate

    @critrate.setter
    def critrate(self, amount):
        self.__critrate = amount

    @property
    def name(self):
        return self.__name
    
    @property
    def turn(self):
        return self.__turn
    
    @turn.setter
    def turn(self, boolean):
        self.__turn = boolean

    @property
    def speed(self):
        self.__speed

    @speed.setter
    def speed(self, amount):
        self.__speed = amount
