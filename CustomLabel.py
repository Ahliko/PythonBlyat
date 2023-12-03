import pygame


class Label:
    def __init__(self, text: str, size: int, color: tuple[int, int, int], pos: tuple[int, int],
                 font_name: str = None,
                 center: bool = False):
        self.__text = text
        self.__color = color
        self.__pos = pos
        self.__font_name = font_name
        self.__font = pygame.font.Font(font_name, size)
        self.__center = center
        self.__label = self.__font.render(self.__text, 1, self.__color)

        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__label, self.__rect)

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, new_text: str) -> None:
        self.__text = new_text
        self.__label = self.__font.render(self.__text, 1, self.__color)

    @property
    def center(self) -> bool:
        return self.__center

    @center.setter
    def center(self, new_center: bool) -> None:
        self.__center = new_center
        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        self.__size = new_size
        self.__font = pygame.font.Font(self.__font_name, self.__size)
        self.__label = self.__font.render(self.__text, 1, self.__color)
        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color
        self.__label = self.__font.render(self.__text, 1, self.__color)
        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, new_pos):
        self.__pos = new_pos
        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)

    @property
    def font_name(self):
        return self.__font_name

    @font_name.setter
    def font_name(self, new_font_name):
        self.__font_name = new_font_name
        self.__font = pygame.font.Font(self.__font_name, self.__size)
        self.__label = self.__font.render(self.__text, 1, self.__color)
        if self.__center:
            self.__rect = self.__label.get_rect(center=self.__pos)
        else:
            self.__rect = self.__label.get_rect(topleft=self.__pos)
