from core import Config, Runtime
from Draw import Draw
from Ui import Button
import pygame

__all__ = [
    "Config",
    "Runtime",
    "Draw",
    "Button"
]

def set_display(width: int, height: int, flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0):
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

def init():
    pass