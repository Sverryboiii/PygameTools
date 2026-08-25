from pytools.Collide import Collide
from typing import Any
import pygame

class DropDown:
    def __init__(
            self,
            rect: pygame.Rect,
            display: pygame.Surface,
            choices: list[Any],
            color: pygame.Color | tuple[int, int, int] = (50, 50, 50)
    ):
        self.rect = rect
        self.display = display
        self.color = color
        self.choices = choices
        self.choice_rects = []
        for i in range(len(self.choices)):
            self.choice_rects.append(pygame.Rect(
                self.rect.x,
                self.rect.y + i*self.rect.h,
                self.rect.w,
                self.rect.h
            ))

        self.selected: Any = None
        self.opened: bool = False

    def draw(self) -> None:
        pygame.draw.rect(
            surface=self.display,
            color=self.color,
            rect=self.rect,
            border_radius=10,
        )
        pygame.draw.rect(
            surface=self.display,
            color=(
                self.color[0] + 30,
                self.color[1] + 30,
                self.color[2] + 30
            ),
            rect=self.rect,
            border_radius=10,
            width=3
        )

        if not self.opened:
            return

        for rect in self.choice_rects:
            pygame.draw.rect(
                surface=self.display,
                color=(
                    self.color[0] + 30,
                    self.color[1] + 30,
                    self.color[2] + 30
                ),
                rect=rect,
                border_radius=10,
                width=3
            )
            pygame.draw.rect(
                surface=self.display,
                color=(
                    self.color[0] + 60,
                    self.color[1] + 60,
                    self.color[2] + 60
                ),
                rect=rect,
                border_radius=10,
                width=3
            )

    def events(self) -> Any | None:
        mp = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.opened and click:
            for count, rect in enumerate(self.choice_rects):
                if not Collide.rect_point(rect, mp):
                    continue
                self.selected = self.choices[count]
                self.opened = False

        if Collide.rect_point(self.rect, mp) and click:
            self.opened = not self.opened
        elif click:
            self.opened = False

        return None

    def update(self) -> Any | None:
        value = self.events()
        self.draw()
        return value