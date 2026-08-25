# PygameTools
A module that sets up some basics for pygame usage.

Components:
 - Ui Elements (In Development)
 - Runtime function with configurations (In Development)

On initializing you can choose a lot of things such as the display size, font, base fps, etc. (In Development)
Base configurations:
 - FPS: 60
 - TPS: 20
 - Frame Update Function: A screen that says welcome.
 - Font: Arial, size=32

There are 2 runtime functions named "frame" and "tick":
"frame" gets executed every frame. Here lays the graphic system.
"tick" gets executed less than frame (mostly 3x less). In tick lays path-finding, physics and inputs.
Warning: The tick is very basic code that will stop when your frame stops. Therefore you must make your own system when you want to make the frame and tick synchronized!
