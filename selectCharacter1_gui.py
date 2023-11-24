import pygame as pg
from main_menu_gui import MainMenu
import pygame_widgets
from CustomButton import Button
from CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class CharacterMenu1():
    def __init__(self, previous_menu: MainMenu):
        self.previous_menu = previous_menu
        self.settings_menu = None
        self.__quit = False

    def disable(self):
        self.__quit = True
        pg.event.wait(100)

    def update_screen(self, **kwargs):
        self.previous_menu.ecran.blit(self.previous_menu.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.previous_menu.ecran)

    def on_click_next(self):
        print("Next")
    def on_click_back(self):
        print("Back")
    def on_click_choice1(self):
        print("you choose 1")
    def on_click_choice2(self):
        print("you choose 2")
    def on_click_choice3(self):
        print("you choose 3")

    def update_screen(self, **kwargs):
        self.previous_menu.ecran.blit(self.previous_menu.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.previous_menu.ecran)

    def run(self):
        pg.display.set_caption('PythonBlyat - SelectCharacter1')
        bouton_next = Button((self.previous_menu.largeur / 2) + 615, (self.previous_menu.hauteur / 2) + 360, 130, 40, self.previous_menu.font, 'Next',
                             self.on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.previous_menu.largeur / 2) - 745, (self.previous_menu.hauteur / 2) + 360, 130, 40, self.previous_menu.font, 'Back',
                             self.on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button((self.previous_menu.largeur / 2) - 450, (self.previous_menu.hauteur / 2), 130, 40, self.previous_menu.font, 'Choice1',
                             self.on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.previous_menu.largeur / 2) - 60, (self.previous_menu.hauteur / 2), 130, 40, self.previous_menu.font, 'Choice2',
                                self.on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.previous_menu.largeur / 2) + 350, (self.previous_menu.hauteur / 2), 130, 40, self.previous_menu.font, 'Choice3',
                                self.on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0), (self.previous_menu.largeur / 2, self.previous_menu.hauteur / 2 - 300), None, True)
        label_selection = Label("Choose your character1", 50, (0, 0, 0), (self.previous_menu.largeur / 2, self.previous_menu.hauteur / 2 - 150),
                                None, True)
        self.update_screen(next=bouton_next, back=bouton_back, choice1=bouton_choice1, choice2=bouton_choice2, choice3=bouton_choice3, title=label_title, text=label_selection)
        pg.display.flip()
        while not self.__quit:
            self.previous_menu.clock.tick(self.previous_menu.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    print("Touche Echap")
                    pg.quit()
                    exit()
                elif event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.update_screen(next=bouton_next, back=bouton_back, choice1=bouton_choice1, choice2=bouton_choice2, choice3=bouton_choice3, title=label_title, text=label_selection)
            pygame_widgets.update(events)
            pg.display.update()