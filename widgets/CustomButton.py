import pygame

class Button:
    def __init__(self, x, y, width, height, font, button_text='Button', onrelease_function=None,
                 one_press=False, fill_colors=('#3E3E3E', '#666666', '#333333'), center=False, hide=False):
        self.width = width
        self.height = height
        self.onreleaseFunction = onrelease_function
        self.onePress = one_press
        self.__hide = hide
        self.__text = button_text
        self.__center = center
        self.alreadyPressed = False
        self.normal_color = '#3E3E3E'
        self.__font = font
        self.fillColors = {
            'normal': fill_colors[0],
            'hover': fill_colors[1],
            'pressed': fill_colors[2],
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))

        if center:
            self.x = x - self.width // 2
            self.y = y - self.height // 2
        else:
            self.x = x
            self.y = y

        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = self.__font.render(self.__text, True, (20, 20, 20))

    def draw(self, screen):
        if self.__hide:
            return
        mouse_pos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                print("Button clicked")
                self.buttonSurface.fill(self.fillColors['pressed'])
                self.alreadyPressed = True
            elif self.alreadyPressed:
                print("Button pressed")
                if self.onePress:
                    self.onreleaseFunction()
                else:
                    self.onreleaseFunction()
                self.alreadyPressed = False
        else:
            if self.alreadyPressed:
                print("reverse")
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

    def hide(self):
        self.__hide = True

    def show(self):
        self.__hide = False

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value
        self.buttonSurf = self.__font.render(self.__text, True, (20, 20, 20))

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, value):
        self.__center = value
        if self.__center:
            self.x = self.x - self.width // 2
            self.y = self.y - self.height // 2
        else:
            self.x = self.x + self.width // 2
            self.y = self.y + self.height // 2
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update_pos(self, x, y):
        self.x = x
        self.y = y
        if self.__center:
            self.x = self.x - self.width // 2
            self.y = self.y - self.height // 2
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
