from sverpykit.Collide import Collide
from sverpykit.Draw import Draw
from sverpykit.core import Config
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
        self.hitbox_offset = (0, 0)

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

        self.selected: Any = ""
        self.opened: bool = False
        self.pressed: bool = False

    def draw(self, display=None) -> None:
        if not display:
            display = self.display

        Draw.draw_rect(
            display=display,
            color=self.color,
            rectangle=self.rect,
            border_radius=10,
        )
        Draw.draw_rect(
            display=display,
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
            ),
            display=display
        )

        if not self.opened:
            return

        for c, rect in enumerate(self.choice_rects):
            Draw.draw_rect(
                display=display,
                color=(
                    min(255, self.color[0] + 30),
                    min(255, self.color[1] + 30),
                    min(255, self.color[2] + 30)
                ),
                rectangle=rect,
                border_radius=10
            )
            Draw.draw_rect(
                display=display,
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
            Draw.draw_surface(text, (rect.x+10, rect.y-3), display=display)

    def events(self) -> Any | None:
        mp = pygame.mouse.get_pos()
        click = False
        for event in Config.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if not click:
            self.pressed = False

        if self.opened and click:
            for count, rect in enumerate(self.choice_rects):
                if not Collide.rect_point(pygame.Rect(
                    self.rect.x + self.hitbox_offset[0],
                    self.rect.y + self.hitbox_offset[1],
                    self.rect.w,
                    self.rect.h
                ), mp):
                    continue
                self.selected = self.choices[count]
                self.opened = False

        if Collide.rect_point(pygame.Rect(
            self.rect.x + self.hitbox_offset[0],
            self.rect.y + self.hitbox_offset[1],
            self.rect.w,
            self.rect.h
        ), mp) and click:
            if self.pressed:
                return False
            self.opened = not self.opened
            self.pressed = True
        elif click:
            self.opened = False

        return None

    def update(self, check_events: bool = True) -> Any | None:
        value = None
        if check_events: value = self.events()
        self.draw()
        return value