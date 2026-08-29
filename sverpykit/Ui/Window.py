import pygame
from sverpykit.core import Config
from sverpykit.Draw import Draw

class Window:
    def __init__(
            self,
            owner: list,
            rect: pygame.Rect,
            components: list,
            color: tuple[int, int, int] =  (150, 150, 150)
    ):
        self.owner = owner

        self.rect = rect
        self.components = components
        self.color = color

    def events(self):
        mp, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]
        if self.owner[0] is not self:
            if self.rect.collidepoint(mp) and click:
                self.owner.remove(self)
                self.owner.append(self)
            return

    def draw(self):
        Draw.draw_rect(
            display=Config.screen,
            color=self.color,
            rectangle=self.rect,
            border_radius=10
        )
