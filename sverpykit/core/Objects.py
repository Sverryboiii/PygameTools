import pygame

def create_rect(
        x: int | float,
        y: int | float,
        width: int | float,
        height: int | float
) -> pygame.Rect:
    """
    This is the same
    :param x: The x position of the rectangle.
    :param y: The y position of the rectangle.
    :param width: The width of the rectangle.
    :param height: The height of the rectangle.
    :return: Returns a pygame rectangle.
    """
    return pygame.Rect(x, y, width, height)