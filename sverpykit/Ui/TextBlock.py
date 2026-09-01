from sverpykit.Draw import Draw
from sverpykit.core import Config
import pygame

text_block_font = pygame.font.SysFont("airal", 25)

class TextBlock:
    def __init__(
        self,
        rect: pygame.Rect,
        text: str
    ):
        self.rect = rect
        self.text = text
        self.text_surf = [text_block_font.render(str(part), True, Config.BEIGE) for part in text.split("\n")]

    def draw(self, display):
        for c, surf in enumerate(self.text_surf):
            display.blit(surf, (self.rect.x, self.rect.y + c*25))

    def events(self):
        pass

    def change_text(self, text: str):
        self.text = text
        self.text_surf = [Draw.render_text(str(part)) for part in text.split("\n")]
