from sverpykit.Collide import Collide
from sverpykit.Draw import Draw
from sverpykit.core import Config
import pygame
from typing import Any, Callable

class SearchBar:
    def __init__(
            self,
            *args,
            rect: pygame.Rect,
            display: pygame.Surface,
            function: Callable = lambda : None,
            color: pygame.Color | tuple[int, int, int] = (50, 50, 50),
            **kwargs
    ):
        self.rect: pygame.Rect = rect
        self.hitbox_offset = (0, 0)

        self.display: pygame.Surface = display
        self.color: pygame.Color | tuple[int, int, int] = color

        self.stored: str = ""
        self.last_stored: str = ""
        self.stored_surf: pygame.Surface = Config.font.render(self.stored, True, Config.BEIGE)

        self.selected: bool = False

        self.function = function
        self.args = args
        self.kwargs = kwargs

    def draw(self, display=None) -> None:
        if not display:
            display = self.display

        color = self.color
        if self.selected:
            color = (
                min(255, color[0] + 30),
                min(255, color[1] + 30),
                min(255, color[2] + 30)
            )
        Draw.draw_rect(
            display=display,
            color=color,
            rectangle=self.rect,
            border_radius=int(self.rect.h/2)
        )
        Draw.draw_rect(
            display=display,
            color=(
                min(255, color[0] + 30),
                min(255, color[1] + 30),
                min(255, color[2] + 30)
            ),
            rectangle=self.rect,
            border_radius=int(self.rect.h/2),
            width=3
        )
        Draw.draw_surface(self.stored_surf, (
            self.rect.x + self.rect.w/2 - self.stored_surf.get_width()/2,
            self.rect.y + self.rect.h/2 - self.stored_surf.get_height()/2
        ), display=display)

    def events(self) -> Any:
        click = False
        for event in Config.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True
        mp = pygame.mouse.get_pos()

        if self.selected:
            for event in Config.events:
                if event.type != pygame.KEYDOWN:
                    continue
                if event.key == pygame.K_BACKSPACE:
                    self.stored = self.stored[:-1]
                elif event.key == pygame.K_KP_ENTER:
                    self.function(self.stored, *self.args, **self.kwargs)
                elif event.unicode.isprintable():
                    self.stored += event.unicode

        if self.stored != self.last_stored:
            self.stored_surf = Draw.render_text(self.stored)
        self.last_stored = self.stored

        if not click:
            return

        if Collide.rect_point(
            rect=pygame.Rect(
                self.rect.x + self.hitbox_offset[0],
                self.rect.y + self.hitbox_offset[1],
                self.rect.w,
                self.rect.h
            ),
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