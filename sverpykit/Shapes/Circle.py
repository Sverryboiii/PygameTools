import pygame

class Circle:
    def __init__(
            self,
            center: tuple[int, int],
            diameter: int
    ):
        self.center = center
        self.diameter = diameter

    def draw(
            self,
            display: pygame.Surface,
            color: tuple[int, int, int]
    ) -> None:
        pygame.draw.circle(
            surface=display,
            color=color,
            center=self.center,
            radius=self.diameter/2
        )