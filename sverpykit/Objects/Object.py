from sverpykit.core import Config, Runtime
from typing import Callable, Any
import pygame

class Object:
    def __init__(
            self,
            hitbox: pygame.Rect,
            surface: pygame.Surface,
            events: dict[str, Callable] | None = None,
            statistics: dict[str, Any] | None = None,
            states: dict[str, Any] | None = None,
            resize_surface: bool = True
    ):
        events = events if isinstance(events, dict)\
            else {}
        statistics = statistics if isinstance(statistics, dict)\
            else {}
        states = states if isinstance(states, dict)\
            else {}
        self.hitbox = hitbox
        self.surface = surface
        if resize_surface:
            self.surface = pygame.transform.scale(surface, (hitbox.w, hitbox.h))

        self.states: dict[str, str | int | float | bool | dict[str, str | int | float | bool]] = {
            "surface": "solid", # Will be used later with slippery and bouncy.
            "physics": {
                "enabled": False,
                "terminal_velocity": 1 # This is a multiplier, but 0 = off (Keep speeding up forever).
            },
            "vy": 0.0,
            "vx": 0.0,
            "show_hitbox": False
        }
        self.states.update(states)

        self.stats = {
            "speed": 100,
            "jump_power": 15
        }
        self.stats.update(statistics)

        self.accepted_events = {
            "key": Object.key_events,
            "mouse": Object.mouse_events,
            "random": Object.random_event
        }
        self.accepted_events.update(events)

        self.standing_on: Object | None = None
        self.on_ground = False

    def key_events(self, keys: dict):
        pass

    def mouse_events(self, button: int, pos: tuple[int, int]):
        pass

    def random_event(self, number):
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

    def physics(self):
        mass = self.hitbox.w * self.hitbox.h
        terminal_velocity = mass * Config.terminal_velocity
        self.states["vy"] = min(terminal_velocity, max(-terminal_velocity, self.states["vy"] - Config.delta_time * Config.gravity))

        friction_force_x = int(
            Config.slippery_friction if self.standing_on.states["surface"] == "slippery" else Config.solid_friction* (mass * Config.gravity)
        ) if self.standing_on else Config.air_friction
        if self.states["vx"] > 0:
            self.states["vx"] = max(0, self.states["vx"] - friction_force_x)
        if self.states["vx"] < 0:
            self.states["vx"] = min(0, self.states["vx"] + friction_force_x)

        self.hitbox.y -= self.states["vy"] * Config.delta_time * Config.gravity
        self.check_y_collision()
        self.hitbox.x += self.states["vx"] * Config.delta_time * Config.gravity
        self.check_x_collision()

    def events(self):
        click = pygame.mouse.get_pressed()
        mp = pygame.mouse.get_pos()
        if any(click):
            self.accepted_events["mouse"](self, click, mp)
        keys = pygame.key.get_pressed()
        if any(keys):
            self.accepted_events["key"](self, keys)
        if self.states["physics"]:
            self.physics()

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
            if obj is self:
                continue

            if self.states["vx"] > 0:
                self.hitbox.x = obj.hitbox.x - self.hitbox.w
                reset_velocity = True
            elif self.states["vx"] < 0:
                self.hitbox.x = obj.hitbox.x + obj.rect.w
                reset_velocity = True

        if reset_velocity:
            self.states["vx"] = 0

    def check_y_collision(self) -> None:
        """
        This check should be run after every time you update the y-position of the entity.
        """

        self.on_ground = False
        reset_velocity = False
        collides_on = None

        for obj in Runtime.game_objects:
            print(hasattr(obj, "collides"))
            if not hasattr(obj, "collides"):
                continue
            if not obj.collides(self.hitbox):
                continue
            if obj is self:
                continue

            if self.states["vy"] > 0:
                self.hitbox.y = obj.hitbox.y + obj.hitbox.h
                reset_velocity = True
            elif self.states["vy"] < 0:
                self.hitbox.y = obj.hitbox.y - self.hitbox.h
                reset_velocity = True
                collides_on = obj
                self.on_ground = True

        if reset_velocity:
            self.states["vy"] = 0
        self.standing_on = collides_on

    def collides(self, hitbox: pygame.Rect):
        return self.hitbox.colliderect(hitbox)