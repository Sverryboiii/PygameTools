import pygame

# WINDOW
screen: pygame.Surface

def set_display(display: pygame.Surface) -> None:
    global screen
    screen = display
    print(screen)