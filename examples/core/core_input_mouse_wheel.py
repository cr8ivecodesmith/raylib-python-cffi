"""

raylib [core] example - Mouse wheel input

"""
from raylib.pyray import PyRay
from raylib.colors import (
    RAYWHITE,
    GRAY,
    LIGHTGRAY,
    MAROON,
)


pyray = PyRay()


# Initialization
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

pyray.init_window(SCREEN_WIDTH, SCREEN_HEIGHT,
                  'raylib [core] example - input mouse wheel')

box_position_y: int = SCREEN_HEIGHT // 2 - 40
scroll_speed = 4  # Scrolling speed in pixels

pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second


# Main game loop
while not pyray.window_should_close():  # Detect window close button or ESC key
    # Update
    box_position_y -= (pyray.get_mouse_wheel_move() * scroll_speed)

    # Draw
    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)

    pyray.draw_rectangle(
        SCREEN_WIDTH // 2 - 40, box_position_y, 80, 80, MAROON)

    pyray.draw_text('User mouse wheel to move the cube up and down!',
                    10, 10, 20, GRAY)
    pyray.draw_text('Box position Y: {:03d}'.format(box_position_y),
                    10, 40, 20, LIGHTGRAY)

    pyray.end_drawing()


# De-Initialization
pyray.close_window()  # Close window and OpenGL context
