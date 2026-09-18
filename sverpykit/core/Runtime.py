from sverpykit.Ui.Window import Window
from sverpykit.Ui.TextBlock import TextBlock
from sverpykit.core import Config
import pygame, sys, os
from pathlib import Path

ui_layers = []
game_objects = []

def load_image(
        path: str,
        name: str
) -> pygame.Surface:
    """
    :param path: The path to your file (Be sure this is a full path!).
    :param name: The name that the image gets stored to.
    :return: Returns the image, but also saves it in sverpykit's cache.
    """
    img = pygame.image.load(path)
    Config.images[name] = img
    return img

def resize_image(
        name: str,
        width: int | float,
        height: int | float,
        save: bool = True
) -> pygame.Surface:
    """
    :param name: This is the same name as where you loaded the image.
    :param width: The width of the resized surface.
    :param height: The height of the resized surface.
    :param save: Decides if the image will be cached with or without changes.
    :return: Returns the resized image.
    """
    img = pygame.transform.scale(Config.images[name], (width, height))
    if save:
        Config.images[name] = img
    return img

def rotate_image(
        name: str,
        rotation: float | int,
        save: bool = False
) -> pygame.Surface:
    """
    :param name: This is the same name as where you loaded the image.
    :param rotation: The rotation of the new image in degrees.
    :param save: Decides if the image will be cached with or without changes.
    :return: Returns the rotated image.
    """
    img = pygame.transform.rotate(
        Config.images[name],
        rotation
    )
    if save:
        Config.images[name] = img
    return img

def add_layer(
        layer_type: str,
        rectangle: pygame.Rect,
        components: list,
        color: tuple[int, int, int] = (150, 150, 150),
        **kwargs
) -> Window:
    """
    :return: Returns nothing.
    """
    w = Window(ui_layers, rectangle, components, color, **kwargs)
    for component in w.components:
        if isinstance(component, TextBlock):
            component.owner = w
    ui_layers.append(w)
    return w

def add_game_object(obj):
    """
    :param obj: The object that gets added.
    :return: Returns nothing.
    """
    game_objects.append(obj)

tick_counter = 0
def register_tick() -> None:
    global tick_counter
    tick_counter -= Config.delta_time
    while tick_counter < 0:
        Config.events = pygame.event.get()
        tick_counter += 1 / Config.tick_rate

        for event in Config.events:
            if event.type == pygame.QUIT:
                Config.exit_function()

        Config.tick_function()
        for layer in reversed(ui_layers):
            if layer.events(): break
        [obj.events() for obj in game_objects]

def update():
    """
    Used for start, but can also be called to update 1 frame.
    :return:
    """
    Config.delta_time = Config.clock.tick(Config.max_fps) / 1000
    register_tick()

    Config.screen.fill(Config.background_color)
    Config.frame_function()
    [layer.draw() for layer in ui_layers]
    [obj.draw() for obj in game_objects]

    pygame.display.flip()

def start() -> None:
    """
    Makes the main game loop so you don't have to.
    Features:
     - Main loop
     - Events
     - FPS control
     - Updating the screen
     - Resetting the screen

    You can change almost all of these!
    """
    while True:
        update()