from pytools.Collide import Collide
from pytools.Draw import Draw
from pytools.core import Config
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
                self.rect.y + i*self.rect.h + self.rect.h,
                self.rect.w,
                self.rect.h
            ))

        self.selected: Any = None
        self.opened: bool = False
        self.pressed: bool = False

    def draw(self) -> None:
        Draw.draw_rect(
            display=self.display,
            color=self.color,
            rectangle=self.rect,
            border_radius=10,
        )
        Draw.draw_rect(
            display=self.display,
            color=(
                self.color[0] + 30,
                self.color[1] + 30,
                self.color[2] + 30
            ),
            rectangle=self.rect,
            border_radius=10,
            width=3
        )

        Draw.draw_surface(
            Draw.render_text(
                str(self.selected),
                True,
                Config.BEIGE
            ), (
                self.rect.x+10, self.rect.y-3
            )
        )

        if not self.opened:
            return

        for c, rect in enumerate(self.choice_rects):
            Draw.draw_rect(
                display=self.display,
                color=(
                    min(255, self.color[0] + 30),
                    min(255, self.color[1] + 30),
                    min(255, self.color[2] + 30)
                ),
                rectangle=rect,
                border_radius=10
            )
            Draw.draw_rect(
                display=self.display,
                color=(
                    min(255, self.color[0] + 60),
                    min(255, self.color[1] + 60),
                    min(255, self.color[2] + 60)
                ),
                rectangle=rect,
                border_radius=10,
                width=3
            )
            text = Draw.render_text(
                text=str(self.choices[c]),
                antialias=True,
                color=Config.BEIGE
            )
            Draw.draw_surface(text, (rect.x+10, rect.y-3))

    def events(self) -> Any | None:
        print(self.pressed)
        mp = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if not click:
            self.pressed = False

        if self.opened and click:
            for count, rect in enumerate(self.choice_rects):
                if not Collide.rect_point(rect, mp):
                    continue
                self.selected = self.choices[count]
                self.opened = False

        if Collide.rect_point(self.rect, mp) and click and not self.pressed:
            self.opened = not self.opened
            self.pressed = True
        elif click:
            self.opened = False

        return None

    def update(self) -> Any | None:
        value = self.events()
        self.draw()
        return value