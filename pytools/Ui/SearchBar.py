from pytools.Collide import Collide
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
        self.rect: pygame.Rect = rect
        self.display: pygame.Surface = display
        self.color: pygame.Color | tuple[int, int, int] = color

        self.selected: bool = False

    def draw(self) -> None:
        color = self.color
        if self.selected:
            color = (min(255, c + 30) for c in color)
        Draw.draw_rect(
            display=self.display,
            color=color,
            rectangle=self.rect,
            border_radius=int(self.rect.h/2)
        )
        Draw.draw_rect(
            display=self.display,
            color=color,
            rectangle=self.rect,
            border_radius=int(self.rect.h/2),
            width=3
        )

    def events(self) -> Any:
        click = pygame.mouse.get_pressed()[0]
        mp = pygame.mouse.get_pos()

        if not click:
            return

        if Collide.rect_point(
            rect=self.rect,
            point=mp
        ):
            self.selected = True
        else:
            self.selected = False

    def update(self, check_events: bool = True):
        value = None
        if check_events:
            value = self.events()
        self.draw()
        return value