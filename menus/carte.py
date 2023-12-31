import pygame
import pytmx
import pyscroll
from lib.game import Game


class Carte:
    def __init__(self, game: Game):
        pygame.display.set_caption('PythonBlyat - Carte Donjon')
        self.clock = pygame.time.Clock()
        self.__game = game
        self.__quit = False

        tmx_data = pytmx.util_pygame.load_pygame("assets/carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.__game.ecran.get_size())
        self.map_layer.zoom = 6

        player_position = tmx_data.get_object_by_name("Player")
        self.player = Player(player_position.x, player_position.y, self)

        self.monsters = [Monster(i.x, i.y) for i in tmx_data.objects if
                         i.type == "Monster"]

        vendor_position = tmx_data.get_object_by_name("Vendor")
        self.vendor = Vendor(vendor_position.x, vendor_position.y)

        self.walls = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects if
                      obj.type == "wall"]

        self.fin = [pygame.Rect(obj.x, obj.y, obj.width, obj.height) for obj in tmx_data.objects if
                    obj.type == "Fin"]

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=3)
        self.group.center(self.player.rect.center)
        self.group.add(self.player)
        for i in self.monsters:
            self.group.add(i)
        self.group.add(self.vendor)

    @property
    def game(self):
        return self.__game

    def get_collision_sprite(self):
        for i in self.monsters:
            if self.check_collision(self.player, [i]):
                return i

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

    @staticmethod
    def check_collision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self):
        self.__game.update_display()
        self.map_layer.set_size(self.__game.ecran.get_size())
        self.group.update()
        self.player.animate()
        for i in self.monsters:
            i.animate()
        self.vendor.animate()
        pygame.display.flip()
        for sprite in [self.group.sprites()[0]]:
            if sprite.feet.collidelist(self.walls) > -1:
                pygame.event.wait(self.__game.framerate * 100 // 6)
                self.__game.play_sound_bump()
                sprite.move_back()

    def shop(self):
        self.__game.stop_sound_donjon()
        pygame.event.wait(self.__game.framerate * 100 // 6)
        from menus.shop_gui import ShopMenu
        shop = ShopMenu(self.__game)
        shop.run()
        self.__game.play_sound_donjon()

    def lose(self):
        self.__game.stop_sound_donjon()
        from menus.lose import Lose
        lose = Lose(self.game)
        lose.run()

    def win(self):
        self.__game.stop_sound_donjon()
        from menus.win import Win
        win = Win(self.game)
        win.run()

    def check_win(self):
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.fin) > -1:
                pygame.event.wait(self.__game.framerate * 100 // 6)
                self.win()

    def run(self):
        self.__game.play_sound_donjon()
        while True:
            self.check_win()
            self.player.save_location()
            for i in self.monsters:
                i.save_location()
            self.vendor.save_location()
            self.handle_input()
            self.__game.handle_fullscreen()
            self.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.__game.ecran)
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.clock.tick(60)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, carte):
        super().__init__()
        self.carte = carte
        self.sprite_sheet = pygame.image.load("assets/test3.png")
        self.__space_image_width = 16
        self.__space_image_height = 32
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.speed = 2
        self.sleep = 0
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
        if self.sleep == 10:
            self.sleep = 0
            self.current_image += 1

            if self.current_image >= len(self.images[self.direction]):
                self.current_image = 0

            self.image = self.images[self.direction][self.current_image]
        else:
            self.sleep += 1

    def change_direction(self, direction):
        self.direction = direction

    def save_location(self):
        self.old_position = self.position.copy()

    def start_fight(self):
        self.carte.game.stop_sound_donjon()
        from menus.fight_gui import FightMenu
        fight = FightMenu(self.carte.game)
        result = fight.run()
        self.carte.game.play_sound_donjon()
        return result

    def move_right(self):
        if not self.carte.check_collision(self, self.carte.monsters):
            if not self.carte.check_collision(self, [self.carte.vendor]):
                self.position[0] += self.speed
            else:
                self.position[0] -= self.speed * 2
                self.carte.shop()
        else:
            monster = self.carte.get_collision_sprite()
            self.position[0] -= self.speed * 2
            if self.start_fight():
                self.carte.monsters.remove(monster)
                monster.kill()
            else:
                self.carte.lose()

    def move_left(self):
        if not self.carte.check_collision(self, self.carte.monsters):
            if not self.carte.check_collision(self, [self.carte.vendor]):
                self.position[0] -= self.speed
            else:
                monster = self.carte.get_collision_sprite()
                self.position[0] += self.speed * 2
                self.carte.shop()
        else:
            monster = self.carte.get_collision_sprite()
            self.position[0] += self.speed * 2
            if self.start_fight():
                self.carte.monsters.remove(monster)
                monster.kill()
            else:
                self.carte.lose()

    def move_up(self):
        if not self.carte.check_collision(self, self.carte.monsters):
            if not self.carte.check_collision(self, [self.carte.vendor]):
                self.position[1] -= self.speed
            else:
                self.position[1] += self.speed * 2
                self.carte.shop()
        else:
            monster = self.carte.get_collision_sprite()
            self.position[1] += self.speed * 2
            if self.start_fight():
                self.carte.monsters.remove(monster)
                monster.kill()
            else:
                self.carte.lose()

    def move_down(self):
        if not self.carte.check_collision(self, self.carte.monsters):
            if not self.carte.check_collision(self, [self.carte.vendor]):
                self.position[1] += self.speed
            else:
                self.position[1] -= self.speed * 2
                self.carte.shop()
        else:
            monster = self.carte.get_collision_sprite()
            self.position[1] -= self.speed * 2
            if self.start_fight():
                self.carte.monsters.remove(monster)
                monster.kill()
            else:
                self.carte.lose()

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


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("assets/monster.png")
        self.__space_start_image_width = 0
        self.__space_start_image_height = 1
        self.__space_image_width = 32
        self.__space_image_height = 32 + 1
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.sleep = 0
        self.position = [x - 16, y - 16]
        self.speed = 2
        self.current_image = 0
        self.direction = 'idle'
        self.images = {
            'idle': [
                self.get_image(self.__space_start_image_width, self.__space_start_image_height),
                self.get_image(self.__space_image_width, self.__space_start_image_height),
                self.get_image(self.__space_image_width * 2, self.__space_start_image_height),
                self.get_image(self.__space_image_width * 3, self.__space_start_image_height),
                self.get_image(self.__space_image_width * 4, self.__space_start_image_height),
                self.get_image(self.__space_start_image_width, self.__space_image_height),
                self.get_image(self.__space_image_width, self.__space_image_height),
                self.get_image(self.__space_image_width * 2, self.__space_image_height),
                self.get_image(self.__space_image_width * 3, self.__space_image_height),
                self.get_image(self.__space_image_width * 4, self.__space_image_height),
                self.get_image(self.__space_start_image_width, self.__space_image_height * 2),
                self.get_image(self.__space_image_width, self.__space_image_height * 2),
                self.get_image(self.__space_image_width * 2, self.__space_image_height * 2),
            ]
        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def animate(self):
        if self.sleep == 10:
            self.sleep = 0
            self.current_image += 1

            if self.current_image >= len(self.images[self.direction]):
                self.current_image = 0

            self.image = self.images[self.direction][self.current_image]
        else:
            self.sleep += 1

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


class Vendor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("assets/vendor.png")
        self.__space_start_image_width = 32
        self.__space_start_image_height = 0
        self.__space_image_width = 32
        self.__space_image_height = 32 + 1
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.sleep = 0
        self.position = [x, y]
        self.speed = 1
        self.current_image = 0
        self.direction = 'Idle'
        self.images = {
            'Idle': [
                self.get_image(self.__space_start_image_width, self.__space_start_image_height),
                self.get_image(self.__space_start_image_width + self.__space_image_width,
                               self.__space_start_image_height),
                self.get_image(self.__space_start_image_width + self.__space_image_width * 2,
                               self.__space_start_image_height),
                self.get_image(self.__space_start_image_width + self.__space_image_width * 3,
                               self.__space_start_image_height)
            ]
        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def save_location(self):
        self.old_position = self.position.copy()

    def animate(self):
        if self.sleep == 10:
            self.sleep = 0
            self.current_image += 1

            if self.current_image >= len(self.images[self.direction]):
                self.current_image = 0

            self.image = self.images[self.direction][self.current_image]
        else:
            self.sleep += 1

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([self.__space_image_width, self.__space_image_height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.__space_image_width, self.__space_image_height))
        image.set_colorkey((0, 0, 0))
        return image


if __name__ == '__main__':
    pygame.init()
    test = Carte(Game())
    test.run()
