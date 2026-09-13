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

        offset_y = 0
        for surf in self.text_surfs:
            Draw.draw_surface(
                surf, (
                    self.rect.x, self.rect.y + offset_y
                ),
                display = display
            )
            offset_y += surf.get_height()

    def events(self):
        pass

    def change_text(self, text: str):
        self.text = text
        self.text_surfs = [Draw.render_text(part, name=self.font) for part in text.split("\n")]

    def add_text(self, text: str, font: str, color: tuple[int, int, int]):
        self.text = self.text + "\n" + text
        self.text_surfs.append(Draw.render_text(text, True, color, font))
