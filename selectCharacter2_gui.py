import pygame as pg
from main_menu_gui import MainMenu
from CustomButton import Button
from CustomLabel import Label
from Environnement_ecran import EnvironnementEcran


class CharacterMenu2():
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        self.__quit = False
        self.texte_rect = None
        self.texte = None
        self.font = None
        self.__background = pg.image.load("mainmenu_background.jpg")
        self.__surface = pg.Surface((200, 200))

    @property
    def background(self):
        return self.__background

    def change_font(self, font: str, taille: int):
        self.font = pg.font.SysFont(font, taille)

    def afficher_texte(self, texte: str, couleur: tuple[int, int, int], position: tuple[int, int],
                       border_thickness: int = 5, border_color: tuple[int, int, int] = (255, 0, 0)):
        self.texte = self.font.render(texte, True, couleur)
        self.texte_rect = self.texte.get_rect()
        self.texte_rect.center = position
        border_rect = pg.Rect(self.texte_rect.left - border_thickness,
                              self.texte_rect.top - border_thickness,
                              self.texte_rect.width + 2 * border_thickness,
                              self.texte_rect.height + 2 * border_thickness)
        pg.draw.rect(self.ecran, border_color, border_rect)
        self.ecran.blit(self.texte, self.texte_rect)
        pg.display.flip()

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
        self.ecran.blit(self.background, (0, 0))
        for i in kwargs:
            kwargs[i].draw(self.ecran)

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - SelectCharacter2')
        bouton_next = Button((self.largeur / 2) + 615, (self.hauteur / 2) + 360, 130, 40, self.font, 'Next',
                             self.on_click_next, False, ('#2a75a1', '#666666', '#333333'))
        bouton_back = Button((self.largeur / 2) - 745, (self.hauteur / 2) + 360, 130, 40, self.font, 'Back',
                             self.on_click_back, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice1 = Button((self.largeur / 2) - 450, (self.hauteur / 2), 130, 40, self.font, 'Choice1',
                             self.on_click_choice1, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice2 = Button((self.largeur / 2) - 60, (self.hauteur / 2), 130, 40, self.font, 'Choice2',
                                self.on_click_choice2, False, ('#2a75a1', '#666666', '#333333'))
        bouton_choice3 = Button((self.largeur / 2) + 350, (self.hauteur / 2), 130, 40, self.font, 'Choice3',
                                self.on_click_choice3, False, ('#2a75a1', '#666666', '#333333'))
        label_title = Label("PythonBlyat", 100, (0, 0, 0), (self.largeur / 2, self.hauteur / 2 - 300), None, True)
        label_selection = Label("Choose your character2", 50, (0, 0, 0), (self.largeur / 2, self.hauteur / 2 - 150), None, True)
        self.update_screen(next=bouton_next, back=bouton_back, choice1=bouton_choice1, choice2=bouton_choice2, choice3=bouton_choice3, title=label_title, text=label_selection)
        pg.display.flip()
        while not self.__quit:
            self.clock.tick(self.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__quit = True
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.__quit = True
            self.update_screen(next=bouton_next, back=bouton_back, choice1=bouton_choice1, choice2=bouton_choice2, choice3=bouton_choice3, title=label_title, text=label_selection)
            pg.display.update()
        pg.quit()
        exit()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
