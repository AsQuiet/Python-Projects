
class InputField():

    def __init__(self, max_x, max_y):

        self.max_x = max_x
        self.max_y = max_y

        self.data = [] # array of strings representing the inputed text

        self.display_y = 0 # from what line should we start drawing the data (len(data) - max_y) >= 0

        self.cursor_x = 0
        self.cursor_y = 0

        self.generate_buffer(max_x, max_y)

    def set_max(self, x, y):
        self.max_x = x
        self.max_y = y
    
    def add_char(self, char):

        new_s = self.set_str_index(
            self.data[self.cursor_y],
            self.cursor_x,
            char)

        self.data[self.cursor_y] = new_s
    
    def advance(self):
        """Should, in most cases be called after add_char."""
        self.cursor_x += 1
        if self.cursor_x >= self.max_x:
            self.cursor_x = 0
            self.cursor_y += 1

    
    def set_cursor(self, x=None, y=None):
        self.cursor_x = x if x != None else self.cursor_x
        self.cursor_y = y if y != None else self.cursor_y
    
    def generate_buffer_string(self, length):
        s = ''
        for x in range(length):
            s += ' '
        return s

    def generate_buffer(self, width, height):
        self.data.clear()
        for y in range(height):
            self.data.append(self.generate_buffer_string(width))
    
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

    i = InputField(100, 25)

    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()

    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()

    i.add_char("q")
    i.advance()
    i.add_char("q")

    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")

    i.advance()
    i.add_char("q")
    i.advance()
    i.add_char("q")
    i.advance()
    
    
    
    print(i.data)

    

main()


