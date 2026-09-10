from sverpykit.Draw import Draw
import pygame

class TextBlock:
    def __init__(
            self,
            rect: pygame.Rect,
            text: str,
            font: str = "default"
    ):
        self.rect = rect
        self.text_surf = Draw.render_text(str(text), name=font)

    def draw(self):
        Draw.draw_surface(
            self.text_surf, (
                self.rect.x, self.rect.y
            ),
        )

    def change_text(self, text: str):
        self.text_surf = Draw.render_text(str(text))