from sverpykit.Shapes import Circle
import pygame, math

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

def circle_circle(
        circle1: Circle.Circle,
        circle2: Circle.Circle
) -> bool:
    """
    :param circle1: The first circle.
    :param circle2: The second circle.
    :return: Returns if the circles collide.
    """
    return math.sqrt(
        math.pow(circle1.center[0] - circle2.center[0], 2) + math.pow(circle1.center[1] - circle2.center[1], 2)
    ) < circle1.diameter/2 + circle2.diameter/2