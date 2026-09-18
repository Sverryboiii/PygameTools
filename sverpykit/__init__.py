# Core
import pygame
pygame.init()
from .core import Config, Runtime
from .core.Runtime import add_layer, add_game_object, start, update as run_frame, load_image
from .core.Config import default_exit as quit_game
from .core.initialize import set_display, set_frame_method, set_font, set_quit_method, set_tick_method,\
    set_src_path, max_rate

# File Management
from .core import Json
from .core.FileManager import resource_path

# Collision
from .Collide.Collide import collides

# Drawing
from .Draw.Draw import draw_surface, draw_rect, draw_circle, render_text
from .Objects.Entity import Entity
from .Objects.Block import Platform

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
