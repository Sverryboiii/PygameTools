from sverpykit.core import Config
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
        self.text = text
        self.text_surfs = [Draw.render_text(str(text), name=font)]
        self.font = font

    def draw(self, display):
        display = display if display is not None else Config.screen
        [Draw.draw_surface(
            surf, (
                self.rect.x, self.rect.y + c * Config.fonts[self.font].get_height()
            ),
            display=display
        ) for c, surf in enumerate(self.text_surfs)]

    def events(self):
        pass

    def change_text(self, text: str):
        self.text = text
        self.text_surfs = [Draw.render_text(part, name=self.font) for part in text.split("\n")]
