from pytools.Draw import Draw
import pygame, sys
from typing import Callable

def default_exit():
    pygame.quit()
    sys.exit()

welcome_text = pygame.font.SysFont("arial", 100).render("Welcome!", True, (255, 255, 255))
def frame():
    pygame.transform.scale(welcome_text, (screen.get_width(), screen.get_height()))
    Draw.draw_surface(welcome_text, (0, 0))

def tick():
    pass

# WINDOW
screen: pygame.Surface

# Events
max_fps: int | float = 60
tick_rate: int | float = 20
events: list[pygame.event.Event] = []
clock: pygame.time.Clock = pygame.time.Clock()
delta_time: int

# Functions
exit_function: Callable = default_exit
frame_function: Callable = frame
tick_function: Callable = tick

# Ui
font: pygame.font.Font

# Colors
background_color: pygame.Color | tuple[int, int, int] = (25, 25, 25)

# Color names
BEIGE = (220, 245, 245)