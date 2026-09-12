from sverpykit.core import Config
from typing import Callable, Any
import pygame

class Entity:
    def __init__(
            self,
            hitbox: pygame.Rect,
            surface: pygame.Surface,
            player_events: dict[str, Callable] | None = None,
            statistics: dict[str, Any] | None = None,
            states: dict[str, Any] | None = None
    ):
        player_events = player_events if isinstance(player_events, dict)\
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
            "key": self.key_events,
            "mouse": self.mouse_events
        }
        self.accepted_events.update(player_events)

    def key_events(self, keys: dict):
        pass

    def mouse_events(self, button, pos):
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
        self.hitbox.y -= self.states["vy"] * Config.delta_time
        click = pygame.mouse.get_pressed()
        mp = pygame.mouse.get_pos()
        if any(click):
            self.accepted_events["mouse"](click, mp)
        keys = pygame.key.get_pressed()
        if any(keys):
            self.accepted_events["key"](keys)