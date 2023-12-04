import pygame
from widgets.CustomLabel import Label


class ListLabel(Label):
    def __init__(self, title: str, text_list: list[str], size: int, color: tuple[int, int, int], pos: tuple[int, int],
                 font_name: str = None,
                 center: bool = False):
        super().__init__(title, size, color, pos, font_name, center)
        self.__text_list = text_list
        self.__labels: list[Label] = []
        for i, text in enumerate(self.__text_list):
            label = Label(text, size, color, (pos[0], pos[1] + i * size), font_name, center)
            self.__labels.append(label)

    def draw(self, screen: pygame.Surface) -> None:
        for label in self.__labels:
            label.draw(screen)

    @property
    def text(self) -> list[str]:
        return self.__text_list

    @text.setter
    def text(self, new_text_list: list[str]) -> None:
        self.__text_list = new_text_list
        self.__labels = []
        for i, text in enumerate(self.__text_list):
            label = Label(text, self.size, self.color, (self.pos[0], self.pos[1] + i * self.size),
                          self.font_name, self.center)
            self.__labels.append(label)

    def append(self, text: str):
        self.__text_list.append(text)
        self.text = self.__text_list

    def remove(self, text: str):
        if text in self.__text_list:
            self.__text_list.remove(text)
            self.text = self.__text_list

    def update_pos_all(self, x, y):
        self.pos = (x, y)
        for i, label in enumerate(self.__labels):
            if self.center:
                label.center = True
            else:
                label.center = False
            label.update_pos(self.pos[0], self.pos[1] + i * self.size)

