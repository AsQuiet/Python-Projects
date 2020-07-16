
import tkinter as tk 
 
class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        entry = tk.Entry(self) 
        entry.bind("<FocusIn>", self.print_type)  
        entry.bind("<Key>", self.print_key) 
        entry.pack(padx=20, pady=20) 
 
    def print_type(self, event): 
        print(event.type) 
 
    def print_key(self, event): 
        args = event.keysym, event.keycode, event.char 
        print("Symbol: {}, Code: {}, Char: {}".format(*args)) 
 
if __name__ == "__main__": 
    app = App() 
    app.mainloop() 

import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tk.END, quote)
tk.mainloop()