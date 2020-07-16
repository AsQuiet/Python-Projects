import tkinter as tk


class Win():

    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height

        self.root = tk.Tk('main')

        self.inputfield = tk.Text(self.root, width=width, height=height)    # used for handling event
        self.inputfield.bind('<KeyRelease>', self.handle_input)
        self.inputfield.pack()
    
    def handle_input(self, event):
        sym = event.keysym
        # keycode = event.keycode
        char = event.char

        print("got char " + str(char) + " and symbol " + str(sym))

        curser_index = float(self.inputfield.index(tk.INSERT))
        print(curser_index)

        if char == '(':
            self.inputfield.insert(tk.INSERT, ')')
            # self
            # .inputfield.mark_set(tk.INSERT, "%d.%d" % (x,int(curser_index)))
            self.inputfield.mark_set(tk.INSERT, )
        elif char == '[':
            self.inputfield.insert(tk.INSERT, ']')
        elif char == '{':
            self.inputfield.insert(tk.INSERT, '}')
        





        

            

    
    def start(self):
        self.root.mainloop()




win = Win()
win.start()





    

        