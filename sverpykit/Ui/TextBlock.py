from sverpykit.Draw import Draw
import pygame

class TextBlock:
    def __init__(
        self,
        rect: pygame.Rect,
        text: str
    ):
        self.rect = rect
        self.text = text
        self.text_surf = [Draw.render_text(str(part)) for part in text.split("\n")]

    def draw(self, display):
        [Draw.draw_surface(surf, (self.rect.x, self.rect.y), display=display) for surf in self.text_surf]

    def change_text(self, text: str):
        self.text = text
        self.text_surf = [Draw.render_text(str(part)) for part in text.split("\n")]
