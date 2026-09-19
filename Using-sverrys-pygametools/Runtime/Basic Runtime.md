# Basic Runtime
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

# Runtime Functions:

## Images:
There are a few image functions.
### `load_image(path, name)`:
This function loads an image.<br>
Parameters:<br>
\- `path`: Where the image that you want to load is located.<br>
\- `name`: What name we save the loaded image on (Warning: If the place that you save the
image to already contains an image this data will be overwritten!).<br>
### `resize_image(name, width, height, save)`:
This function resizes an image to the wanted size.<br>
Parameters:<br>
\- `name`: The name where you saved the image.<br>
\- `width`: The new width of the image.<br>
\- `height`: The new height of the image.<br>
\- `save`: Decides if we save the resized image (True) or keep the old image (False).<br>
Warning: Resizing images may cause pixels to misform!
### `rotate_image(name, rotation, save)`:
This function rotates an image to the wanted angle.<br>
\- `name`: The name where you saved the image.<br>
\- `rotation`: The angle that this image gets rotated to.<br>
\- `save`: Decides if we save the rotated image (True) or keep the old image (False).<br>
Warning: Rotating images may cause pixels to misform!
