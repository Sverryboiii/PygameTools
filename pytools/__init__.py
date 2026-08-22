from .core import Config, Runtime
from .core.initialize import set_display, set_frame_method, set_font, set_quit_method, set_tick_method,\
    max_rate, start
from .Draw import Draw
from .Ui import Button
import pygame
pygame.init()

__all__ = [
    "Config",
    "Runtime",
    "Draw",
    "Button"
]