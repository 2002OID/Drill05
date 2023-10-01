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

def make_arrow():
    global x, y, arrow_x, arrow_y
    if x == arrow_x and y == arrow_y:
        arrow_x = random.randint(0, TUK_WIDTH + 1)
        arrow_y = random.randint(0, TUK_HEIGHT + 1)
    hand_arrow.draw(arrow_x, arrow_y)

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    make_arrow()
    #go_cha_to_arr()
    update_canvas()
    frame = (frame + 1) % 8

close_canvas()
