from __future__ import annotations
import random

random.seed()

class Character:
    
    def __init__(self, name: str, max_health: int, atk: int, _def: int) -> None:
        self._name = name
        self._maxhp = max_health
        self._hp = max_health
        self._atk = atk
        self._def = _def
        self._shield = 0
        self._critdmg = 50 # dégats crit %
        self._critrate = 5 # chances de coup crit
        self._ultime = 0

    def __str__(self):
        return f"name : {self._name}, HPMAX : {self._maxhp}, HP {self._hp}, ATK : {self._atk}, DEF : {self._def}, TC : {self._critrate}, DC : {self._critdmg}"

    def is_alive(self):
        return self._hp > 0

    def compute_damages(self):
       nb = random.randint(0, 100)
       if nb <= self._critrate:
           return self._atk + (self._atk * (self._critdmg/100))
       else :
           return self._atk

    def compute_wounds(self, damages):
        return damages - self._def
    
    def attack(self, target : Character):
        if not self.is_alive():
            return
        damages = int(self.compute_damages())
        print(f"⚔️ {self._name} attack with {damages} damages in your face ! (attack: {self._atk})")
        self._ultime += 10
        target.defense(damages)

    def defense(self, damages):
        wounds = self.compute_wounds(damages)
        print(f"🛡️ {self._name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self._def})")
        self.decrease_health(wounds)

    def decrease_health(self, amount):
        if self._shield > 0:
            self._shield -= amount
            if self.shield < 0:
                self._hp += self._shield
                self._shield = 0
        else :
            self._hp =- amount