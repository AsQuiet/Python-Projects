import tkinter as tk
import string_lib as sl
import os, sys

class Win():

    OPP_AND_CENTER_CURSOR = 1 # eg: when char == '(' => add ')' and center cursor between the two

    def __init__(self, width=80, height=24):
        self.width = width
        self.height = height

        self.root = tk.Tk('main')
        self.root.title('vinyl - untitled')

        self.inputfield = tk.Text(self.root, width=width, height=height-1,borderwidth = 1,relief="flat",highlightthickness=0) 
        self.inputfield.config(tabs=('1c', '2c'))
        self.inputfield.bind('<KeyRelease>', self.handle_input)
        self.inputfield.pack(fill=tk.BOTH, expand=True)

        self.command_line = tk.Entry(self.root, width = width)
        self.command_line.bind('<KeyRelease>', self.handle_command_line_input)
        self.command_line.pack(fill=tk.X, side=tk.BOTTOM)
        self.command_function = lambda cmd : None   # temp function => will be set by contol class

        # options
        self.center_and_opp = {}

        self.global_options = {
            'path' : ''
        }

          
    def handle_input(self, event):
        sym = event.keysym
        char = event.char

        print("got char " + str(char) + " and symbol " + str(sym))

        curser_index = float(self.inputfield.index(tk.INSERT))
        print(curser_index)

        # looking for any options this char might have to do something with
        if char in self.center_and_opp.keys():
            self.inputfield.insert(tk.INSERT, self.center_and_opp[char])
            self.inputfield.mark_set(tk.INSERT, curser_index)

        # CTRL-P
        if 'p' not in char and sym == 'p':
            self.focus_on_cmd()
        
    def handle_command_line_input(self, event):
        symbol = event.keysym

        if symbol == "Return":
            if self.command_function != None:
                self.command_function(self.command_line.get())
        elif symbol == 'Escape':
            self.focus_on_inputfield()
        
    def set_inputfield(self, text):
        self.inputfield.delete('1.0', tk.END)

        for line in text:
            self.inputfield.insert(tk.END, line)

    def focus_on_inputfield(self, event=None):
        self.inputfield.focus_set()
    
    def focus_on_cmd(self, event=None):
        self.command_line.focus_set()
    
    def set_cmd(self, text):
        self.command_line.delete('0', tk.END)
        self.command_line.insert(tk.END, text)

    def add_key_listener(self, char, event, char2=None):

        if event == Win.OPP_AND_CENTER_CURSOR:
            self.center_and_opp[char] = char2
    
    def start(self):
        self.root.mainloop()