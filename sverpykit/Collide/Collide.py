from sverpykit.Shapes import Circle
import pygame, math

class collides:

    @ staticmethod
    def rect_rect(
            rect1: pygame.Rect,
            rect2: pygame.Rect
    ) -> bool:
        return rect1.colliderect(rect2)

    @ staticmethod
    def rect_point(
            rect: pygame.Rect,
            point: tuple[int, int]
    ) -> bool:
        return rect.collidepoint(point)

    @ staticmethod
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

    @ staticmethod
    def circle_point(
            circle: Circle.Circle,
            point: tuple[int, int]
    ) -> bool:
        """
        :param circle: The circle.
        :param point: The coordinates of the point.
        :return: Returns if the coordinates are in the circle.
        """
        return math.sqrt(
            math.pow(circle.center[0] - point[0], 2) + math.pow(circle.center[1] - point[1], 2)
        ) < circle.diameter

    # @ staticmethod
    # def circle_rect(
    #         circle: Circle.Circle,
    #         rect: pygame.Rect
    # ) -> bool:
    #     """
    #     :param circle: The circle.
    #     :param rect: The rect.
    #     :return: Returns if the rectangle collides with the circle.
    #     """