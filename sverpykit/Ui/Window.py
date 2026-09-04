import pygame
from sverpykit.core import Config
from sverpykit.Draw import Draw
from sverpykit.Ui.Button import Button

title_bar_height = 30
title_bar_font = pygame.font.SysFont("arial", 30)

class Window:
    def __init__(
            self,
            owner: list,
            rect: pygame.Rect,
            components: list,
            color: tuple[int, int, int] =  (150, 150, 150),
            title_bar: bool = True
    ):
        self.owner = owner

        self.rect = rect
        self.components = components
        self.color = color
        self.title_bar = title_bar
        self.title_bar_rect = pygame.Rect(
            self.rect.x,
            self.rect.y - title_bar_height,
            self.rect.w,
            title_bar_height
        )

        # Events
        self.last_title_bar_touch = None

        self.operational_buttons = [
            Button(
                rect=pygame.Rect(
                    self.rect.x + self.rect.w - title_bar_height * 2,
                    self.rect.y - title_bar_height,
                    title_bar_height,
                    title_bar_height
                ),
                button_color=(50, 50, 50),
                surface=title_bar_font.render("-", True, Config.BEIGE),
                display=Config.screen,
                rounding=int(title_bar_height / 3),
                function=self.minimize
            ),
            Button(
                rect=pygame.Rect(
                    self.rect.x + self.rect.w - title_bar_height,
                    self.rect.y - title_bar_height,
                    title_bar_height,
                    title_bar_height
                ),
                button_color=(50, 50, 50),
                surface=title_bar_font.render("x", True, Config.BEIGE),
                display=Config.screen,
                rounding=int(title_bar_height / 3),
                function=self.close
            )
        ]

        for component in self.components:
            component.hitbox_offset = (self.rect.x, self.rect.y)

    def close(self):
        self.owner.remove(self)

    def minimize(self):
        pass

    def events(self):
        mp, click = pygame.mouse.get_pos(), pygame.mouse.get_pressed()[0]
        if self.owner[-1] is not self:
            if (self.rect.collidepoint(mp) or self.title_bar_rect.collidepoint(mp)) and click:
                self.owner.remove(self)
                self.owner.append(self)
            return


        if self.title_bar:
            if self.last_title_bar_touch:
                x_offset, y_offset = mp[0] - self.last_title_bar_touch[0], mp[1] - self.last_title_bar_touch[1]
                self.rect.x += x_offset
                self.rect.y += y_offset
                self.title_bar_rect.x += x_offset
                self.title_bar_rect.y += y_offset
                for component in self.components:
                    component.hitbox_offset = (self.rect.x, self.rect.y)
                for component in self.operational_buttons:
                    component.rect.x += x_offset
                    component.rect.y += y_offset
            if self.title_bar_rect.collidepoint(mp) and click:
                self.last_title_bar_touch = mp
            else:
                self.last_title_bar_touch = None

        [component.events() for component in self.components]

        return self.rect.collidepoint(mp) or self.title_bar_rect.collidepoint(mp)

    def draw(self):
        Draw.draw_rect(
            display=Config.screen,
            color=self.color,
            rectangle=self.rect,
            border_bottom_left_radius=3,
            border_bottom_right_radius=3
        )
        Draw.draw_rect(
            display=Config.screen,
            color=(
                max(0, self.color[0] - 10),
                max(0, self.color[1] - 10),
                max(0, self.color[2] - 10)
            ),
            rectangle=self.rect,
            border_bottom_left_radius=3,
            border_bottom_right_radius=3,
            width=2
        )

        display = pygame.Surface((self.rect.w, self.rect.h)).convert_alpha()
        display.fill((0,0,0,0))
        [component.draw(display) for component in self.components]
        Draw.draw_surface(display, (self.rect.x, self.rect.y))

        if self.title_bar:
            Draw.draw_rect(
                display=Config.screen,
                color=(200, 200, 200),
                rectangle=self.title_bar_rect,
                border_top_left_radius=3,
                border_top_right_radius=3
            )

            [button.update() for button in self.operational_buttons]
