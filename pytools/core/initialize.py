from pytools.core import Config, Runtime
from typing import Callable, Optional
import pygame

# Automatic initialization
pygame.key.set_repeat(500, 5)

# Manual initialization
def set_display(
        width: int,
        height: int,
        flags: int = 0,
        depth: int = 0,
        display: int = 0,
        vsync: int = 0
) -> pygame.Surface:
    """
    :param width: Width of the screen
    :param height: Height of the screen
    :param flags: Special properties for the display, pygame.RESIZABLE makes the user able to resize the screen.
    :param depth: How many colors you can use (Most of the time 8-bit is good enough. In which case just leave it blank).
    :param display: Decides which monitor is used for the window.
    :param vsync: Caps framerate to the monitor to avoid screen tearing (Screen tearing is just a visual glitch.)
    :return:
    """
    Config.screen = pygame.display.set_mode((width, height), flags, depth, display, vsync)
    return Config.screen

def max_rate(
        fps: int | None = None,
        tick: int | None = None
) -> None:
    """
    :param fps: Caps the max frame rate (Can alwasy go below this number if anything is struggling).
    :param tick: Sets the max tick rate (If the frame rate is lower than the tick rate the ticks will build up, so this is not a cap)
    """
    Config.max_fps = fps if fps else Config.max_fps
    Config.tick_rate = tick if tick else Config.tick_rate

def set_font(
        font: str = "arial",
        size: int = 25,
        bold: bool = False,
        italic: bool = False,
        constructor: Optional[Callable[[Optional[str], int, bool, bool], pygame.font.Font]] = None
) -> pygame.font.Font:
    """
    :param font: The font of the text.
    :param size: How big the font is.
    :param bold: If the font is bold or not.
    :param italic: If the font is italic or not.
    :param constructor: If you like a custom class to be attached to the font.
    :return: Returns the font. Most of the time not needed though.
    """
    Config.font = pygame.font.SysFont(font, size, bold, italic, constructor)
    return Config.font

def set_quit_method(method: Callable) -> None:
    """
    :param method: This method/function gets ran when the player presses Alt + F4 or the X in the top right.
    """
    Config.exit_function = method

def set_frame_method(method: Callable) -> None:
    """
    :param method: This method/function gets ran every frame.
    """
    Config.frame_function = method

def set_tick_method(method: Callable) -> None:
    """
    :param method: This method/function gets ran every tick.
    """
    Config.frame_function = method

def get_delta() -> int | float:
    """
    :return: Returns the time it took for the last frame in ms.
    """
    return Config.delta_time

def start():
    Runtime.start()