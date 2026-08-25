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
    if any([border_top_left_radius, border_top_right_radius, border_bottom_left_radius, border_bottom_right_radius]):
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
        return
    pygame.draw.rect(
        surface=display,
        color=color,
        rect=rectangle,
        width=width,
        border_radius=border_radius
    )

def draw_circle(
        display: pygame.Surface,
        color: pygame.Color | tuple[int, int, int],
        center: tuple[int, int],
        radius: float | int,
        width: int,
        draw_top_left: bool = False,
        draw_top_right: bool = False,
        draw_bottom_left: bool = False,
        draw_bottom_right: bool = False,
):
    """
    :param display: The surface the circle gets drawn on.
    :param color: The color of the circle.
    :param center: The center position of the circle.
    :param radius: The radius of the circle.
    :param width: How thick the edges of the circle are (0 is full circle).

    :param draw_top_left: Decides if pygame draws the top left segment. (If this and the next 3 are False the whole circle gets drawn.
    :param draw_top_right: Decides if pygame draws the top right segment.
    :param draw_bottom_left: Decides if pygame draws the bottom left segment.
    :param draw_bottom_right: Decides if pygame draws the bottom right segment.
    :return:
    """
    pygame.draw.circle(
        surface=display,
        color=color,
        center=center,
        radius=radius,
        width=width,
        draw_top_left=draw_top_left,
        draw_top_right=draw_top_right,
        draw_bottom_left=draw_bottom_left,
        draw_bottom_right=draw_bottom_right
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

def render_text(
        text: str,
        antialias: bool,
        color: pygame.Color | tuple[int, int, int]
) -> pygame.Surface:
    """
    :param text: The text displayed.
    :param antialias: Blends outer edges of the text, so it looks smoother.
    :param color: The color of the text.
    :param background: The color of the background.
    :return: Returns the surface so you can use it in Draw.draw_surface().
    """
    return Config.font.render(
        text=text,
        antialias=antialias,
        color=color
    )