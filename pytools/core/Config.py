import pygame, sys
from typing import Callable

def default_exit():
    pygame.quit()
    sys.exit()

# WINDOW
screen: pygame.Surface

# Events
max_fps: int | float
tick_rate: int | float
events: list[pygame.event.Event] = []
clock: pygame.time.Clock = pygame.time.Clock()
delta_time: int

# Functions
exit_function = default_exit
frame_function: Callable
tick_function: Callable

# Ui
font: pygame.font.Font

# Colors
background_color: pygame.Color | tuple[int, int, int] = (25, 25, 25)