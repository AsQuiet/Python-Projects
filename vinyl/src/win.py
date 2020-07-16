import curses as cs 
from curses import textpad
import math

class Win():

    stdscr = cs.initscr()

    @staticmethod
    def init():
        cs.noecho()
        cs.cbreak()
        Win.stdscr.keypad(True)
        cs.start_color()
        cs.use_default_colors()

    @staticmethod
    def exit():
        cs.echo()
        cs.nocbreak()
        Win.stdscr.keypad(False)
        cs.endwin()

    def __init__(self, blink=True):
        cs.curs_set(1 if blink else 0)      # enabling blinking cursor

        self.themes = {}
    
    def writestr(self, x, y, stri):
        Win.stdscr.addstr(int(y), math.ceil(x), str(stri))
    
    def refresh(self):
        Win.stdscr.refresh()

    def writestr_in_rectangle(self, string, x, y, w, h):
        x_ = (w - x) / 2 - len(string) / 2
        y_ = (h - y) / 2
        self.writestr(x_, y_, string)
    
    def get_max_dimensions(self):
        y,x = Win.stdscr.getmaxyx()
        return x,y
    
    def blink(self, value=True):
        cs.curs_set(value)

    def create_color_theme(self, name, foreground_color, background_color):
        cs.init_pair(len(self.themes.keys()) + 1, foreground_color, background_color)
        self.themes[name] = len(self.themes.keys()) + 1
    
    def set_color(self, name):
        pair_num  = self.themes[name]
        Win.stdscr.attron(cs.color_pair(pair_num))
    
    def remove_color(self, name):
        pair_num  = self.themes[name]
        Win.stdscr.attroff(cs.color_pair(pair_num))
    
    def get_input(self):
        return Win.stdscr.getkey()
    
    def convert_to_str(self, key):
        return cs.ascii.unctrl(key)
    
    def create_textbox(self):
        return textpad.Textbox(Win.stdscr, True)
    
    def clear(self):
        Win.stdscr.clear()


class field():

    def __init__(self):
        self.grid = [[]]

        self.pos_x = 0
        self.pos_y = 0

        self.height = 0
        self.width = 0

    def add_char(self, char):
    
        if self.pos_x < len(self.grid[self.pos_y]) and self.pos_y < self.height:
            self.grid[self.pos_y][self.pos_x] = char
        else:

            while self.pos_y >= self.height:

                self.grid.append([])
                self.height += 1
            
            while self.pos_x >= len(self.grid[self.pos_y]):
                self.grid[self.pos_y].append(" ")
                self.width += 1
            
            self.add_char(char)
    
    def add_str(self, string):

        for x in range(len(string)):
            self.add_char(string[x])
            self.pos_x += 1
    
    def set_char(self, char, x, y):
        x_, y_ = self.pos_x, self.pos_y
        self.set_pos(x,y)
        self.add_char(char)
        self.set_pos(x_, y_)

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y 
        
    
    



#     import curses as cs
# import time

# class Field():
#     """Input field for handling user input."""

#     C_MOVE_UP = 1
#     C_MOVE_DOWN = 2
#     C_MOVE_LEFT = 3
#     C_MOVE_RIGHT = 4

#     C_BACKSPACE = 5
#     C_ADD_CHARACTER = 6

#     def __init__(self):

#         self.cs_x = 0
#         self.cs_y = 1

#         self.field = []
    
    
#     def do_command(self, cmd, other=None):

#         if cmd == Field.C_MOVE_UP:
#             if self.cs_y > 0:
#                 self.cs_y -= 1
#             self.cs_x = 0
#         elif cmd == Field.C_MOVE_DOWN:
#             self.cs_y += 1
#             self.cs_x = 0
#         elif cmd == Field.C_MOVE_LEFT:
#             if self.cs_x > 0:
#                 self.cs_x -= 1
#         elif cmd == Field.C_MOVE_RIGHT:
#             self.cs_x += 1

# def draw_field(field, stdscr):
#     stdscr.clear()
#     max_y, max_x = stdscr.getmaxyx()

#     offset = 0
#     for x in range(len(field.field)):
#         stdscr.addstr(x + offset, 0, field.field[x])
#         if len(field.field[x]) >= max_x:
#             offset += 1

# def main(stdscr):
#     cs.curs_set(1)
#     cs.use_default_colors()
#     cs.start_color()    
#     field = Field()

#     while 1:
#         draw_field(field, stdscr)
        
#         stdscr.move(field.cs_y, field.cs_x)
        
#         ch = stdscr.getch()

#         if ch in (cs.KEY_ENTER, 10, 13):
#             break
#         elif ch == cs.KEY_UP:
#             field.do_command(Field.C_MOVE_UP)
#         elif ch == cs.KEY_DOWN:
#             field.do_command(Field.C_MOVE_DOWN)
#         elif ch == cs.KEY_LEFT:
#             field.do_command(Field.C_MOVE_LEFT)
#         elif ch == cs.KEY_RIGHT:
#             field.do_command(Field.C_MOVE_RIGHT)

#         else:
#             # is character => should be added to field
#             try: 
#                 char = str(cs.ascii.unctrl((ch)))
#                 # field.do_command(Field.C_ADD_CHARACTER, char)
#                 stdscr.addstr(0, 1, char)
#             except:
#                 stdscr.refresh()
    
#         stdscr.refresh()



class keycodes():

    CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']  
    CHARS.extend(['(', ')', '{', '}', '[', ']', '+', '-', '/', '*', '*', '%', '$', '&', 'é', '`', ':', ';', '?', ",", '"', "'", '=', ])

    @staticmethod
    def to_string(key):
        for char in keycodes.CHARS:
            try:
                if key == ord(char):
                    return char
            except:
                continue
        return None


class InputField():

    def __init__(self, max_x, max_y):

        self.max_x = max_x
        self.max_y = max_y

        self.current_width = max_x
        self.current_height = max_y

        self.data = [] # array of strings representing the inputed text

        self.display_y = 0 # from what line should we start drawing the data (len(data) - max_y) >= 0

        self.cursor_x = 0
        self.cursor_y = 0

        self.generate_buffer(max_x, max_y)

    def set_max(self, x, y):
        self.max_x = x
        self.max_y = y
    
    def add_char(self, char):
        print("setting character " + char + " at index " + str(self.cursor_x) + ' add line ' + str(self.cursor_y))  
        new_s = self.set_str_index(
            self.data[self.cursor_y],
            self.cursor_x,
            char)

        self.data[self.cursor_y] = new_s
    
    def advance(self):
        """Should, in most cases be called after add_char."""
        if self.cursor_x + 1 >= self.current_width:
            self.set_cursor(0, self.cursor_y + 1)
        else:
            self.set_cursor(self.cursor_x + 1, None)

    def set_cursor(self, x=None, y=None):
        self.cursor_x = x if x != None else self.cursor_x
        self.cursor_y = y if y != None else self.cursor_y

        xoff, yoff = self.cursor_out_of_bounds()
        self.add_height_buffer(yoff)
        self.add_width_buffer(xoff)
    
    def cursor_out_of_bounds(self):

        x_offset, y_offset = 0, 0
        if self.cursor_y >= self.current_height:
            y_offset = self.cursor_y - self.current_height
        if self.cursor_x >= self.current_width:
            x_offset = self.cursor_x - self.current_width   
        
        return x_offset, y_offset

    def generate_buffer_string(self, length):
        s = ''
        for x in range(length):
            s += ' '
        return s

    def generate_buffer(self, width, height):
        self.data.clear()
        for y in range(height):
            self.data.append(self.generate_buffer_string(width))
    
    def add_width_buffer(self, amount):
        self.current_width += amount
        for x in range(len(self.data)):
            self.data[x] = self.data[x] + self.generate_buffer_string(amount)
    
    def add_height_buffer(self, amount):
        self.current_height += amount
        for x in range(amount):
            self.data.append(self.generate_buffer_string(self.current_width))
    
    def set_str_index(self, s, index, char):
        """set_str_index('foo', 1, 'O') => 'fOo' """
        new_s = ''
        for x in range(len(s)):
            char_ = s[x]
            # print('"' + char + '"' + " - " + str(x))
            if x == index:
                new_s += char
            else:
                new_s += char_
        return new_s


def main():

    i = InputField(6, 2)  
    print(i.data)

    i.add_char("q")
    i.advance()
    i.add_char("u")
    i.advance()
    i.add_char("i")
    i.advance()
    i.add_char("n")
    i.advance()
    i.add_char("t")
    i.advance()
    i.add_char("e")
    i.advance()
    i.add_char("n")
    
    
    i.advance()

    print(i.data)



    

main()


