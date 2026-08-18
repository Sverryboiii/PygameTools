import pygame

# WINDOW
screen: pygame.Surface | None = None

def set_display(display: pygame.Surface) -> None:
    global screen
    screen = display