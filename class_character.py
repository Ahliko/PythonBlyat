from __future__ import annotations
import random

import pygame

from game import Game


class Character:
    def __init__(self, _id: int, name: str, critrate: int, critdamage: int) -> None:
        self.__name: str = name
        self.__maxhp: int = 0
        self.__id: int = _id
        self.__hp: int = self.__maxhp
        self.__atk: int = 0
        self.__def: int = 0
        self.__shield: int = 0
        self.__critdmg: int = critdamage  # dégats crit %
        self.__critrate: int = critrate  # chances de coup crit
        self.__ultpts: int = 0  # points d'ultime
        self.__maxultpts: int = 0
        self.__turn: bool = True  # s'il peut jouer ou non
        self.__speed: int = 0
        self.__cooldown: int = 0
        self.__buf: dict = {
            "id": 0,
            "ability": False,
            "atk": self.__atk,
            "critrate": self.__critrate,
            "critdmg": self.__critdmg,
            "remaining": 0
        }
        random.seed()

    def __str__(self) -> str:
        return (f"id : {self.__id}, name : {self.__name}, HPMAX : {self.__maxhp}, HP {self.__hp}, ATK : {self.__atk}, DEF : {self.__def},"
                f" TC : {self.__critrate}, DC : {self.__critdmg}, needs {self.__maxultpts} ULTPTS")

    def is_alive(self) -> bool:
        if self.__hp <= 0:
            self.__turn = False
            return False
        return True

    def compute_damages(self, game: Game) -> int | float:
        if random.randint(0, 100) <= self.__critrate:
            print("CRIT DAMAGE")
            game.history.append("CRIT DAMAGE")
            sound = pygame.mixer.Sound("assets/critdmg.mp3")
            sound.play()
            return self.__atk + (self.__atk * (self.__critdmg / 100))
        else:
            return self.__atk

    def compute_wounds(self, damages: int) -> int:
        return damages - self.__def

    def add_ultpts(self, amount: int) -> None:
        if (self.__ultpts + amount < self.__maxultpts):
            self.__ultpts += amount
        else:
            print(f"{self.name} : ULTIME READY")
            self.__ultpts = self.__maxultpts

    def check_buffs(self, game: Game) -> None:
        if self not in game.monsters:
            if self.__buf["ability"]:
                if self.__buf["id"] == 1:
                    self.__critdmg -= 20
                elif self.__buf["id"] == 2:
                    self.__critrate -= 35
                elif self.__buf["id"] == 3:
                    self.__atk -= int((self.__atk * (25 / 100)))
                self.__buf["ability"] = False
                self.__buf["id"] = 0
            if self.__buf["remaining"] > 0:
                self.__buf["remaining"] -= 1
            if self.__buf["remaining"] == 0:
                self.__atk = self.__buf["atk"]
                self.__critrate = self.__buf["critrate"]
                self.__critdmg = self.__buf["critdmg"]

    def attack(self, target: Character, game: Game) -> list:
        if not self.is_alive():
            return
        elif not target.is_alive():
            print(f"Impossible d'attaquer {target.name}, il est déjà vaincu!")
            return
        self.add_ultpts(15)
        damages = int(self.compute_damages(game))
        print(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {damages})")
        game.history.append(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {damages})")
        self.check_buffs(game)
        self.turn = False
        target.defense(damages, game)
        return [self.name, Character.name]

    def aoe(self, target: list, game: Game):
        if not self.is_alive():
            return
        damages = int(self.compute_damages(game))
        print(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {self.__atk})")
        game.history.append(f"⚔️ {self.__name} attack with {damages} damages in your face ! (attack: {self.__atk})")
        self.turn = False
        for charac in target:
            charac.defense(damages, game)

    def defense(self, damages: int, game) -> None:
        wounds = self.compute_wounds(damages)
        if wounds < 0:
            wounds = 0
        print(f"🛡️ {self.__name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self.__def})")
        game.history.append(f"🛡️ {self.__name} take {wounds} wounds in his face ! (damages: {damages} - defense: {self.__def})")
        self.add_ultpts(10)
        self.decrease_health(wounds)
        if self.is_alive():
            print(f"{self.__hp} HP restants")

    def decrease_health(self, amount: int) -> None:
        if self.__hp - amount < 0:
            self.__hp = 0
        else:
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
        print(f"DANS LE SETTER : {amount}")
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

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

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
    def ultpts(self) -> int:
        return self.__ultpts

    @ultpts.setter
    def ultpts(self, amount: int) -> None:
        self.__ultpts = amount

    @property
    def maxultpts(self) -> int:
        return self.__maxultpts

    @maxultpts.setter
    def maxultpts(self, amount: int) -> None:
        self.__maxultpts = amount

    @property
    def buf(self):
        return self.__buf

    @property
    def cooldown(self):
        return self.__cooldown

    @cooldown.setter
    def cooldown(self, amount: int) -> None:
        self.__cooldown = amount

    @property
    def id(self):
        return self.__id
