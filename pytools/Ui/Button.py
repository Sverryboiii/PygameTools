from pytools.Draw import Draw
from pytools.core import Config
from typing import Any, Callable
import pygame

class Button:
    def __init__(
            self,
            *args,
            rect: pygame.Rect,
            button_color: tuple[int, int, int] | pygame.Color,

            surface: pygame.Surface,

            display: pygame.Surface,

            function: Callable = lambda : None,
            rounding: int = 0,
            resize_surface: bool = False,
            alpha_surface: bool = True,
            center_surface: bool = True,
            **kwargs
    ):
        """
        :param rect: A rectangle made with pygame.Rect.
        :param button_color: The background color of the button.
        :param display: The surface where the button gets placed on (Most of the time just the base display).
        :param surface: A surface of any kind (Text, Image, Even a surface with a rectangle).
        :param rounding: How much the corners of the button is rounded.
        :param resize_surface: Resize the screen to the highest resolution possible for the button (Could mess up the surface).
        :param alpha_surface: If the background of the surface is invisible (Not needed if the surface is already alpha or
        if you rendered a text).
        :param center_surface: If the surface should be centered or just be at the 0,0 coordinate of the button.
        """

        self.display = display

        self.button_color = button_color

        self.rect = rect
        self.rounding = rounding

        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.surf = surface
        self.resize_surf = resize_surface
        self.alpha_surface = alpha_surface
        self.center_surf = center_surface

        self.pressed = False

    def draw(self) -> None:

        # Background
        Draw.draw_rect(
            display=self.display,
            color=self.button_color if not self.pressed else (
                max(0, self.button_color[0] - 30),
                max(0, self.button_color[1] - 30),
                max(0, self.button_color[2] - 30)
            ),
            rectangle=self.rect,
            border_radius=self.rounding
        )

        # Text
        Draw.draw_surface(
            surface=self.surf,
            destination=(0,0) if not self.center_surf else (
                self.rect.x + self.rect.w/2 - self.surf.get_width()/2,
                self.rect.y + self.rect.h/2 - self.surf.get_height()/2
            )
        )

    def events(self) -> Any | None:
        """
        :return: Will return None unless pressed and released (In that case it will return the returned value of the function)
        """
        mp = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        if self.pressed:
            if not click or not self.rect.collidepoint(mp):
                self.pressed = False
                return self.function(*self.args, **self.kwargs)
            return None

        if not click:
            return None

        if self.rect.collidepoint(mp):
            self.pressed = True
        return None

    def update(self) -> Any | None:
        value = self.events()
        self.draw()
        return value