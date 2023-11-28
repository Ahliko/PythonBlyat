import random

import pygame
import pytmx
import pyscroll


class Test:
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption('PythonBlyat - Test')
        self.clock = pygame.time.Clock()

        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y)

        self.walls = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects if
                      obj.type == "wall"]

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.center(self.player.rect.center)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_direction('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_direction('down')
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_direction('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_direction('right')

    def update(self):
        self.group.update()
        self.player.animate()
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        while True:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.clock.tick(60)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("test3.png")
        self.__space_image_width = 16
        self.__space_image_height = 32
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 2
        self.current_image = 0
        self.direction = 'down'
        self.images = {
            'down': [self.get_image(0, 0), self.get_image(self.__space_image_width, 0),
                     self.get_image(self.__space_image_width * 2, 0), self.get_image(self.__space_image_width * 3, 0)],
            'right': [self.get_image(0, self.__space_image_height),
                      self.get_image(self.__space_image_width, self.__space_image_height),
                      self.get_image(self.__space_image_width * 2, self.__space_image_height),
                      self.get_image(self.__space_image_width * 3, self.__space_image_height)],
            'up': [self.get_image(0, self.__space_image_height * 2),
                   self.get_image(self.__space_image_width, self.__space_image_height * 2),
                   self.get_image(self.__space_image_width * 2, self.__space_image_height * 2),
                   self.get_image(self.__space_image_width * 3, self.__space_image_height * 2)],
            'left': [self.get_image(0, self.__space_image_height * 3),
                     self.get_image(self.__space_image_width, self.__space_image_height * 3),
                     self.get_image(self.__space_image_width * 2, self.__space_image_height * 3),
                     self.get_image(self.__space_image_width * 3, self.__space_image_height * 3)]

        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def animate(self):
        if random.randint(0, 10) % 10 == 0:
            self.current_image += 1

            if self.current_image >= len(self.images[self.direction]):
                self.current_image = 0

            self.image = self.images[self.direction][self.current_image]

    def change_direction(self, direction):
        self.direction = direction

    def save_location(self):
        self.old_position = self.position.copy()

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position.copy()
        self.update()

    def get_image(self, x, y):
        image = pygame.Surface([self.__space_image_width, self.__space_image_height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.__space_image_width, self.__space_image_height))
        image.set_colorkey((0, 0, 0))
        return image


if __name__ == '__main__':
    pygame.init()
    test = Test()
    test.run()
