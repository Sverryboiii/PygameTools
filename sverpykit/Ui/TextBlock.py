from sverpykit.Draw import Draw
import pygame

class TextBlock:
    def __init__(
        self,
        rect: pygame.Rect,
        text: str
    ):
        self.rect = rect
        self.text_surf = Draw.render_text(str(text))

    def draw(self):
        Draw.draw_surface(
            self.text_surf, (
                self.rect.x, self.rect.y
            )
        )

    def change_text(self, text: str):
        self.text_surf = Draw.render_text(str(text))