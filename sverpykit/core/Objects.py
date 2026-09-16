import pygame

def create_rect(
        x: int | float,
        y: int | float,
        width: int | float,
        height: int | float
) -> pygame.Rect:
    """
    This is the same
    :param x: The x position of the rect.
    :param y:
    :param width:
    :param height:
    :return: Returns a pygame rectangle.
    """
    return pygame.Rect(x, y, width, height)