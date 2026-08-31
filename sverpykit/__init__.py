# Core
import pygame
pygame.init()
from .core import Config, Runtime
from .core.Runtime import add_layer, start
from .core.Config import default_exit as quit_game
from .core.initialize import set_display, set_frame_method, set_font, set_quit_method, set_tick_method,\
    max_rate

# Drawing
from .Draw.Draw import draw_surface, draw_rect, draw_circle, render_text

# Ui parts
from .Ui.Button import Button
from .Ui.SearchBar import SearchBar
from .Ui.DropDown import DropDown
from .Ui.Window import Window
from .Ui.TextBlock import TextBlock

__all__ = [
    "Config",
    "Runtime",
    "Draw",
    "Button"
]