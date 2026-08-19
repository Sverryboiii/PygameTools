from .core import Config, Runtime
from .Draw import Draw
from .Ui import Button
from typing import Optional, Callable
import pygame
pygame.init()

def set_display(width: int, height: int, flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> pygame.Surface:
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

def max_fps(fps: int) -> None:
    Config.max_fps = fps

def set_font(
        font: str = "arial",
        size: int = 25,
        bold: bool = False,
        italic: bool = False,
        constructor: Optional[Callable[[Optional[str], int, bool, bool], pygame.font.Font]] = None):
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

__all__ = [
    "Config",
    "Runtime",
    "Draw",
    "Button",
    "set_display"
]