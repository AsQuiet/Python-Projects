import curses as cs 
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
        
    
    