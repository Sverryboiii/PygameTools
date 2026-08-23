from pytools.core import Config
from pytools.Draw import Draw
import pygame
from typing import Any

class SearchBar:
    def __init__(
            self,
            rect: pygame.Rect,
            display: pygame.Surface,
            color: pygame.Color | tuple[int, int, int] = (50, 50, 50)
    ):
        self.rect = rect
        self.display = display
        self.color = color

    def draw(self) -> None:
        Draw.draw_rect(
            display=self.display,
            color=self.color,
            rectangle=self.rect,
            border_radius=int(self.rect.h/2)
        )
        Draw.draw_rect(
            display=self.display,
            color=self.color,
            rectangle=self.rect,
            border_radius=int(self.rect.h/2),
            width=3
        )

    def events(self) -> Any:
        pass

    def update(self):
        value = self.events()
        self.draw()
        return value