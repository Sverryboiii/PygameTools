from pytools.core import Config
import pygame, sys

tick_counter = 0
def register_tick():
    global tick_counter
    tick_counter -= Config.delta_time
    while tick_counter < 0:
        tick_counter += 1 / Config.tick_rate
        Config.tick_function()

def start():
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
        Config.delta_time = Config.clock.tick(Config.max_fps)
        register_tick()

        for event in Config.events:
            if event.type == pygame.QUIT:
                Config.exit_function()

        Config.frame_function()

        pygame.display.flip()