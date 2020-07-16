
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


