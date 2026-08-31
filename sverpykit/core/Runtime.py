from sverpykit.Ui.Window import Window
from sverpykit.core import Config
import pygame

ui_layers = []

def add_layer(
        layer_type: str,
        rectangle: pygame.Rect,
        components: list,
        color: tuple[int, int, int] = (150, 150, 150)
) -> None:
    """
    :param layer_type: Currently possible: Window.
    :param rectangle: x, y, width, height of the layer.
    :param components: A list of UI parts that belong to the layer.
    :param color: The base color of the layer.
    :return: Returns nothing.
    """
    if layer_type.lower() == "window":
        ui_layers.append(Window(ui_layers, rectangle, components, color))

tick_counter = 0
def register_tick() -> None:
    global tick_counter
    tick_counter -= Config.delta_time
    while tick_counter < 0:
        tick_counter += 1 / Config.tick_rate

        for event in Config.events:
            if event.type == pygame.QUIT:
                Config.exit_function()

        Config.tick_function()
        for layer in reversed(ui_layers):
            if layer.events(): break

        Config.events = []

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
        Config.screen.fill(Config.background_color)
        Config.events = pygame.event.get()
        Config.delta_time = Config.clock.tick(Config.max_fps)/1000
        register_tick()

        Config.frame_function()
        [layer.draw() for layer in ui_layers]

        pygame.display.flip()