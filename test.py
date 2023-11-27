import pygame
import pytmx
import pyscroll


class Test:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('PythonBlyat - Test')

        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.center(self.player.rect.center)
        self.group.add(self.player)

    def run(self):
        self.group.center((0, 0))
        while True:
            self.group.draw(self.screen)
            pygame.display.flip()
            self.group.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("WarriorDownDeath.png")
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        image.set_colorkey((0, 0, 0))
        return image

if __name__ == '__main__':
    pygame.init()
    test = Test()
    test.run()
