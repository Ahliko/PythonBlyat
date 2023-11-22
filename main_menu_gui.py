import pygame as pg
import pygame_menu as pm
from Environnement_ecran import EnvironnementEcran


class MainMenu(EnvironnementEcran):
    def __init__(self):
        super().__init__(1920, 1080, (255, 255, 255), 60)
        self.main_menu = None
        self.texte_rect = None
        self.texte = None
        self.font = None
        self.surface = pg.Surface((200, 200))

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

    def on_click_play(self):
        print("Button play clicked")
        self.main_menu.disable()

    def on_click_settings(self):
        from settings_gui import SettingsMenu
        settings_menu = SettingsMenu(self)
        settings_menu.run()

    def run(self):
        pg.font.init()
        self.change_font("Arial", 30)
        pg.display.set_caption('PythonBlyat - MainMenu')
        # button = Button(30, 30, 400, 100, self.font, 'Button One (onePress)', self.on_click_play)
        self.main_menu = pm.Menu('Welcome', self.largeur, self.hauteur, theme=pm.themes.THEME_ORANGE)
        label = self.main_menu.add.label('PythonBlyat', font_size=50)
        self.main_menu.add.button('Play', self.on_click_play)
        self.main_menu.add.button('Settings', self.on_click_settings)
        while self.main_menu.is_enabled():
            self.clock.tick(self.framerate)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    break
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    break

            if self.main_menu.is_enabled():
                self.main_menu.update(events)
            if self.main_menu.is_enabled():
                self.main_menu.draw(self.ecran)
            pg.display.update()
        pg.quit()
        exit()


if __name__ == "__main__":
    menu = MainMenu()
    menu.run()
