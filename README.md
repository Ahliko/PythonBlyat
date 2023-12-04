# PythonBlyat
PythonBlyat is a game project that provides a turn-based combat gameplay experience. The players needs to escape the dungeon to win. The game includes various classes for characters and monsters.

This first version of the game was developped in two weeks for a school project, [some upgrades are planned](#📰-upgrades-planned).


## ⚙️ Installation
To install the projet you need to :
```
git clone https://github.com/Ahliko/PythonBlyat.git
```
Enter the project folder :
```
cd PythonBlyat
```
Before the first run, make sure to :
```
pip install -r requirement.txt
```
and make sure to read the [**First Launch Note**](#🚀-first-launch-note)

And now enjoy the game : 
```
python main.py
```

## 🚀 First Launch Note

Here are a few things you need to know before launching the game :

- It is highly recommanded to read the [**Paths Wiki**](https://github.com/Ahliko/PythonBlyat/wiki/Paths) to understand how each path works.
- There are some knowns issues, but this one is the most common :
    - The game can be **too zoomed**. To avoid this bug, do **Win** + **I**, then "**System**", and make sure that the size of text, apps and others items is on **100%**.
    - If you meet other bugs, feel free to **[report an issue](https://github.com/Ahliko/PythonBlyat/issues)**.
- On the "**Choose character**" screen, you need to **first provide a name** for your character, **then choose the [path](https://github.com/Ahliko/PythonBlyat/wiki/Paths)** you want to play with.
- For more information, please refer to the [**wiki**](https://github.com/Ahliko/PythonBlyat/wiki).

## 📂 Repository Structure

<details closed><summary>Click to extend</summary>

```sh
└── PythonBlyat/
    ├── classes/
    │   ├── characters/
    │   │   ├── class_abundance.py
    │   │   ├── class_harmony.py
    │   │   ├── class_hunt.py
    │   │   └── class_preservation.py
    │   ├── class_character.py
    │   └── monsters/
    │       ├── class_aberration.py
    │       ├── class_chimere.py
    │       ├── class_golem.py
    │       └── class_monster.py
    ├── lib/
    │   ├── Environnement_ecran.py
    │   ├── engine.py
    │   └── game.py
    ├── main.py
    ├── menus/
    │   ├── carte.py
    │   ├── fight_gui.py
    │   ├── lose.py
    │   ├── main_menu_gui.py
    │   ├── selectCharacter1_gui.py
    │   ├── selectCharacter2_gui.py
    │   ├── selectCharacter3_gui.py
    │   ├── settings_gui.py
    │   ├── shop_gui.py
    │   └── win.py
    ├── requirement.txt
    └── widgets/
        ├── CustomButton.py
        ├── CustomLabel.py
        └── CustomListLabel.py

```
---
</details>

## 📰 Upgrades planned

- Global :
    - New name for the game
    - Better visual
    - More settings
    - Saves
- In-Game :
    - How to play
    - Tutorial
    - More stages
    - More ennemies
    - Shop
    - Weapons
    - Inventory
    - XP and Gold
    - Upgrade character stats system
    - More Paths
    - And more...

## 🤝 Contribute & Help us

This project was originally a school project developped in two weeks, but we thought that it could be cool to upgrade it, even if it's now a personal project.

Feel free to help us by sending [**your ideas here**](https://github.com/Ahliko/PythonBlyat/issues).

## ©️ Credits

### Sprites :
The map, character and monsters was found from a non-copyrighted bundle from [**itch.io**](https://itch.io/).

### Songs :
- Main menu : **Ahea! Aho! Desu!** by *Surasshu*
- Shop : **The Penis (Eek!)** by *Surasshu*
- Dungeon theme : **Rebirth Mountain (Ext)** from *Pokemon Black 2 & White 2*
- Fight theme : **Testicular Tango** by *Surasshu*

### Paths (Characters) :
Every path in this game is based on the game **Honkai : Star Rail** developped by **COGNOSPHERE PTE. LTD.**