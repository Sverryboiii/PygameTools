from sverpykit.core import Config
from sverpykit.Draw import Draw
from sverpykit.Ui import Window, SearchBar
from typing import Callable, Any
import pygame

class TextBlock:
    def __init__(
            self,
            rect: pygame.Rect,
            text: str,
            font: str = "default",
            newline: bool = True
    ):
        self.rect = rect
        self.text = text
        self.text_surfs: list[dict] = [{"text": Draw.render_text(str(text), name=font), "newline": newline}]
        self.searchbars: list[SearchBar.SearchBar] = []
        self.font = font

        self.owner = None

        self.scrolled = 0
        self.last_size = 0
        self.pressed = False

    def draw(self, display):
        display = display if display is not None else Config.screen

        offset_x = 0
        offset_y = 0
        searchbars_index = 0
        for payload in self.text_surfs:
            Draw.draw_surface(
                payload["text"], (
                    self.rect.x + offset_x,
                    self.rect.y + offset_y
                ),
                display=display
            )
            if payload.get("hyperlink", None):
                pygame.draw.rect(
                    display,
                    (100, 100, 255),
                    pygame.Rect(
                        offset_x + self.rect.x,
                        offset_y + payload["text"].get_height()-5 + self.rect.y,
                        payload["text"].get_width(),
                        3
                    )
                )
            if payload.get("newline", True):
                offset_y += payload["text"].get_height()
                offset_x = 0
            else:
                offset_x += payload["text"].get_width()

            if payload.get("input", False) and payload["input"][0]:
                sb = self.searchbars[searchbars_index]
                if self.owner:
                    sb.hitbox_offset = (self.owner.rect.x, self.owner.rect.y)
                sb.rect.x = offset_x
                sb.rect.y = offset_y
                searchbars_index += 1
        self.last_size = offset_y
        [sb.draw(display) for sb in self.searchbars]
        [sb.events() for sb in self.searchbars]

    def events(self):
        mp = pygame.mouse.get_pos()
        if self.owner:
            mp = (
                mp[0] - self.owner.rect.x - self.rect.x,
                mp[1] - self.owner.rect.y - self.rect.y
            )
        else:
            mp = (
                mp[0] - self.rect.x,
                mp[1] - self.rect.y
            )
        click = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.MOUSEWHEEL:
                self.scrolled = max(0, min(self.last_size, self.scrolled+event.y))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if not click:
            self.pressed = False
            return
        if self.pressed:
            return
        self.pressed = True

        offset_x = 0
        offset_y = 0
        for payload in self.text_surfs:
            if not payload.get("hyperlink", None):
                if payload.get("newline", True):
                    offset_x = 0
                    offset_y += payload["text"].get_height()
                else:
                    offset_x += payload["text"].get_width()
                continue

            text_rect = pygame.Rect(offset_x, offset_y, payload["text"].get_width(), payload["text"].get_height())

            if text_rect.collidepoint(mp):
                payload["hyperlink"][0](*payload["hyperlink"][1])

            if payload.get("newline", True):
                offset_x = 0
                offset_y += payload["text"].get_height()
            else:
                offset_x += payload["text"].get_width()

    def change_text(self, text: str):
        self.text = text
        self.text_surfs = [{"text": Draw.render_text(part, name=self.font) for part in text.split("\n")}]

    def add_text(
            self,
            text: str,
            font: str,
            color: tuple[int, int, int],
            hyperlink: tuple[Callable, list[Any]] | None = None,
            input_: tuple[bool, Callable, list[Any], str] = (False, lambda : None, [], ""),
            newline: bool = False
    ):
        self.text = self.text + text
        self.text_surfs.append({
            "text": Draw.render_text(text, True, color, font),
            "hyperlink": hyperlink,
            "newline": newline,
            "input": input_
        })
        if input_[0]:
            print(input_)
            self.searchbars.append(SearchBar.SearchBar(
                *input_[2],
                rect=pygame.Rect(0, 0, 200, Config.fonts[self.font].get_height()),
                display=Config.screen,
                function=input_[1],
                preset=input_[3]
            ))

    def reset(self):
        self.text = ""
        self.text_surfs = []
