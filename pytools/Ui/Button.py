from pytools.Draw import Draw
from pytools.core import Config
import pygame

class Button:
    def __init__(
            self,
            rect: pygame.Rect,
            button_color: tuple[int, int, int] | pygame.Color,

            surface: pygame.Surface,

            display: pygame.Surface,
            rounding: int = 0,
            resize_surface: bool = False,
            alpha_surface: bool = True,
            center_surface: bool = True
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

        self.surf = surface
        self.resize_surf = resize_surface
        self.alpha_surface = alpha_surface
        self.center_surf = center_surface

    def update(self) -> None:
        pygame.draw.rect(
            surface=self.display,
            color=self.button_color,
            rect=self.rect,
            border_radius=self.rounding
        )
        Draw.draw_surface(
            surface=self.surf,
            destination=(0,0) if not self.center_surf else (
                self.rect.x + self.rect.w/2 - self.surf.get_width()/2,
                self.rect.y + self.rect.h/2 - self.surf.get_height()/2
            )
        )