# Setting Configurations

All configuration settings with their function and meaning:

### Setting Up The Display:
To set up the display you must use `set_display(width, height)`<br>
This will return the window and save it to your configurations for further use.

### Methods:
You can set up different methods for the main game loop to use.<br>
The following possible methods are:<br>
\- `set_frame_method(method)`: `method` gets executed every frame.<br>
Use case: In your frame method you should only draw.<br>
\- `set_tick_method(method)`: `method` gets executed every tick.<br>
Use case: In your tick method you should put path finding, physics, events, etc.<br>
\- `set_quit_method(method)`: `method` gets executed when the user quits the program.<br>
Use case: In your quit method you can save the user's data and quit using `quit_game()`.

### Fonts:
Currently, you can only save 1 font at a time (This will change in future updates).<br>
Use `set_font()` to save a font.<br>
Parameters:<br>
\- `font`: Decides which font to use (Arial is standard).<br>
\- `size`: Decides the size of the text in px.<br>
\- `bold`: Decides if the letters are bold (thick).<br>
\- `italic`: Decides if the letters are italic (cursive).<br>
\- `constructor`: Attach a custom class to the font to get more data.

### Frame- And Tick-Rate:
Frame and Tick rate: `max_rate(fps, tick)`<br>
This function caps the rate of the FPS and TPS.

To get the time passed between frames in seconds you use `get_delta()`.<br>
(Returns a float or an int).

### Starting The Game:
After you have set all the configurations you want you can use the `start()` function
to start the program. Beware that some function are dependent on some configurations.<br>
It's best practice to have set up a display and a font before you start the application.