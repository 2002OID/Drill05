from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
arrow_x, arrow_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
line_frame = 0
cha_arr = 1
def make_arrow():
    global x, y, arrow_x, arrow_y
    if x == arrow_x and y == arrow_y:
        arrow_x = random.randint(0, TUK_WIDTH + 1)
        arrow_y = random.randint(0, TUK_HEIGHT + 1)

def go_cha_to_arrow():
    global x, y, arrow_x, arrow_y, line_frame

    t = line_frame / 50
    x = (1 - t) * x + t * arrow_x
    y = (1 - t) * y + t * arrow_y



while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    make_arrow()
    hand_arrow.draw(arrow_x, arrow_y)
    go_cha_to_arrow()
    if x > arrow_x:
        cha_arr = 0
    else:
        cha_arr = 1
    character.clip_draw(frame * 100, 100 * cha_arr, 100, 100, x, y)
    update_canvas()
    line_frame = (line_frame + 5) % 50
    frame = (frame + 1) % 8
    delay(0.1)

close_canvas()
