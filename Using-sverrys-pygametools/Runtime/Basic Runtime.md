### Basic Runtime
When you execute `start()` the main loop of your game starts.<br>
Therefor you don't have to make the loop logic.

The loop runs this every frame:<br>
\- Reset the background.<br>
\- Get all user events.<br>
\- Wait for the last frame to end and save the delta time.<br>
\- `register_tick()`*.<br>
\- Check if the user quit exited the application.<br>
\- `frame()`**.<br>
\- Update the display (Show all drawings).

*: `register_tick()` first check if a tick may execute and then executes your
tick function.<br>
**: `frame()` executes your custom frame function.