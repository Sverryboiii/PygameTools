from sverpykit.core import Config, Runtime
from typing import Callable, Any
import pygame

class Entity:
    def __init__(
            self,
            hitbox: pygame.Rect,
            surface: pygame.Surface,
            events: dict[str, Callable] | None = None,
            statistics: dict[str, Any] | None = None,
            states: dict[str, Any] | None = None
    ):
        events = events if isinstance(events, dict)\
            else {}
        statistics = statistics if isinstance(statistics, dict)\
            else {}
        states = states if isinstance(states, dict)\
            else {}
        self.hitbox = hitbox
        self.surface = surface

        self.states = {
            "vy": 0,
            "vx": 0,
            "show_hitbox": False
        }
        self.states.update(states)

        self.stats = {
            "speed": 100,
            "jump_power": 15
        }
        self.stats.update(statistics)

        self.accepted_events = {
            "key": Entity.key_events,
            "mouse": Entity.mouse_events
        }
        self.accepted_events.update(events)

    def key_events(self, keys: dict):
        pass

    def mouse_events(self, button: int, pos: tuple[int, int]):
        pass

    def draw(self):
        Config.screen.blit(
            self.surface, self.hitbox
        )
        if self.states["show_hitbox"]:
            pygame.draw.rect(
                Config.screen,
                (255, 255, 255),
                self.hitbox,
                width=1
            )

    def events(self):
        self.hitbox.y += self.states["vy"] * Config.delta_time
        self.check_y_collision()
        self.hitbox.x += self.states["vx"] * Config.delta_time
        self.check_x_collision()
        click = pygame.mouse.get_pressed()
        mp = pygame.mouse.get_pos()
        if any(click):
            self.accepted_events["mouse"](self, click, mp)
        keys = pygame.key.get_pressed()
        if any(keys):
            self.accepted_events["key"](self, keys)

    def check_x_collision(self) -> None:
        """
        This check should be run after every time you update the x-position of the entity.
        """

        reset_velocity = False

        for obj in Runtime.game_objects:
            if not hasattr(obj, "collides"):
                continue
            if not obj.collides(self.hitbox):
                continue

            if self.states["vx"] > 0:
                self.hitbox.x = obj.rect.x - self.hitbox.w
                reset_velocity = True
            elif self.states["vx"] < 0:
                self.hitbox.x = obj.rect.x + obj.rect.w
                reset_velocity = True

        if reset_velocity:
            self.states["vx"] = 0

    def check_y_collision(self) -> None:
        """
        This check should be run after every time you update the y-position of the entity.
        """

        reset_velocity = False

        for obj in Runtime.game_objects:
            if not hasattr(obj, "collides"):
                continue
            if not obj.collides(self.hitbox):
                continue

            if self.states["vy"] > 0:
                self.hitbox.y = obj.rect.y - self.hitbox.h
                reset_velocity = True
            elif self.states["vy"] < 0:
                self.hitbox.y = obj.rect.y + obj.rect.h
                reset_velocity = True

        if reset_velocity:
            self.states["vy"] = 0