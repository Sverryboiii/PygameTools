from .core import Config, Runtime
from .Draw import Draw
from .Ui import Button
import pygame as _pygame
_pygame.init()
_pygame.key.set_repeat(500, 5)

__all__ = [
    "Config",
    "Runtime",
    "Draw",
    "Button"
]