from win import Win, cs, field
import time
import curses.ascii as ai 

win = Win()
win.init()

f = field()


def print_field():
    Win.stdscr.clear()
    i = 0
    for line in f.grid:
        s = ""
        for char in line:
            s+= char
        win.writestr(0, i, s)
        i += 1

def handle_command(key):

    if key == 'KEY_DOWN':
        f.pos_y += 1
        return True
    if key == 'KEY_UP':
        f.pos_y += -1 if f.pos_y > 0 else 0
        return True
    if key == 'KEY_LEFT':
        f.pos_x += -1 if f.pos_x > 0 else 0
        return True
    if key == 'KEY_RIGHT':
        f.pos_x += 1
        return True
    if key == "^J":
        f.pos_y += 1
        f.pos_x = 0

    return False
while True:
    
    print_field()
    Win.stdscr.move(f.pos_y, f.pos_x)
    key = win.get_input()
    try:
        key = win.convert_to_str(key)
    except:
        win.writestr(0, 10, "hello")

    if handle_command(key):
        continue

    if key == "^P":
        break
    
    elif key == "^H":
        # f.pos_x -= 1 if f.pos_x > 0 else 0
        if f.pos_x == 0:
            f.pos_y += -1 if f.pos_y > 0 else 0
            f.pos_x = len(f.grid[f.pos_y])
        else:
            f.pos_x -= 1
        f.add_char(" ")

    elif key[0] != "^":
        f.add_char(key)
        f.pos_x += 1
    
    win.refresh()


time.sleep(0.5)
win.exit()

