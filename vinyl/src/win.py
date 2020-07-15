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


    
        
    
    