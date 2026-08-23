import pygame

def rect_rect(
        rect1: pygame.Rect,
        rect2: pygame.Rect
):
    return rect1.colliderect(rect2)

def rect_point(
        rect: pygame.Rect,
        point: tuple[int, int]
):
    return rect.collidepoint(point)