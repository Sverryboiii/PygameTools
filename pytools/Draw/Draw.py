from pytools.core import Config
import pygame

def draw_rect(
        display: pygame.Surface,
        color: tuple[int, int, int] | pygame.color.Color,
        rectangle: pygame.Rect,
        width: int = 0,
        border_radius: int = 0,
        border_top_left_radius: int = 0,
        border_top_right_radius: int = 0,
        border_bottom_left_radius: int = 0,
        border_bottom_right_radius: int = 0
) -> None:
    """
    :param display: The output surface.
    :param color: The color of the rectangle.
    :param rectangle: The dimensions of the rectangle.
    :param width: The width of the rectangle border (Turns the rectangle itself into the border).
    :param border_radius: The rounding of all corners.
    :param border_top_left_radius: The rounding of the top-left corner.
    :param border_top_right_radius: The rounding of the top-right corner.
    :param border_bottom_left_radius: The rounding of the bottom-left corner.
    :param border_bottom_right_radius: The rounding of the bottom-right corner.
    """
    pygame.draw.rect(
        surface=display,
        color=color,
        rect=rectangle,
        width=width,
        border_radius=border_radius,
        border_top_left_radius=border_top_left_radius,
        border_top_right_radius=border_top_right_radius,
        border_bottom_left_radius=border_bottom_left_radius,
        border_bottom_right_radius=border_bottom_right_radius
    )

def draw_surface(
        surface: pygame.Surface,
        destination: tuple[float | int, float | int],
        area: pygame.Rect | None = None,
        special_flags: int = 0
) -> None:
    """
    :param surface: The surface to draw the surface on.
    :param destination: The x and y coordinate of the surface.
    :param area: Where the surface gets cut off.
    :param special_flags: How the colors are shown.
    """
    Config.screen.blit(
        source=surface,
        dest=destination,
        area=area,
        special_flags=special_flags
    )