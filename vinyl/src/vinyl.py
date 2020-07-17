from win import Win
from control import Control
    
win = Win()
control = Control(win)
win.command_function = control.command

win.add_key_listener('(', Win.OPP_AND_CENTER_CURSOR, ')')
win.add_key_listener('{', Win.OPP_AND_CENTER_CURSOR, '}')
win.add_key_listener('[', Win.OPP_AND_CENTER_CURSOR, ']')
win.add_key_listener('"', Win.OPP_AND_CENTER_CURSOR, '"')
win.add_key_listener("'", Win.OPP_AND_CENTER_CURSOR, "'")

win.start()





    

        