import pygame

class Platform:
    def __init__(
            self,
            rect: pygame.Rect,
            surface: pygame.Surface,
            display: pygame.Surface,
            resize_surface: bool = True
    ):
        self.rect = rect
        self.surface = pygame.transform.scale(
            surface, (self.rect.w, self.rect.h)
        ) if resize_surface else surface
        self.display = display

    def draw(self, display: pygame.Surface | None = None):
        display = display if display else self.display

        display.blit(
            self.surface, self.rect
        )

    def events(self):
        pass

    def collides(self, rect: pygame.Rect):
        return self.rect.colliderect(rect)