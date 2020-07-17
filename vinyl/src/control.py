import tkinter as tk
import string_lib as sl
import os, sys

class Control():
    """Handles the command line of vinyl."""

    def __init__(self, win):
        self.win = win

    def command(self, text):
        print('got command : ' + text)
        command = sl.list_separator(text, ' ')

        if command[0] == 'open':
            self.open_file(command)
        elif command[0] == 'save':
            self.save_file(command)

    def open_file(self, cmd):

        try:
            if '-c' in cmd:
                path = cmd[1]
            else:
                path = os.path.join(self.win.global_options["path"], cmd[1])

            f = open(path, 'r')
            lines = []
            for line in f:
                lines.append(line)
            f.close()

            self.win.set_inputfield(lines)
            self.win.root.title("vinyl - " + cmd[1])
        except:
            self.win.set_cmd('invalid')
    
    def save_file(self, cmd):
    
        try:
            if '-c' in cmd:
                path = cmd[1]
            else:
                path = os.path.join(self.win.global_options["path"], cmd[1])

            f = open(path, 'w')
            print('sd')
            lines = self.win.inputfield.get('1.0', tk.END)
            print(lines)
            for line in lines:
                f.write(line)
            f.close()

            self.win.set_inputfield(lines)
            self.win.root.title("vinyl - " + cmd[1])
        except:
            self.win.set_cmd('invalid')