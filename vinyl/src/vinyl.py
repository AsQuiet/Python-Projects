from win import Win, cs
import time

win = Win()
win.init()
win.blink(False)

mx, my = win.get_max_dimensions()
win.writestr(1, 1, mx)
win.writestr(1, 2, my)



win.create_color_theme("basic", cs.COLOR_BLACK, cs.COLOR_WHITE)

win.set_color("basic")
win.writestr_in_rectangle("continue", 0, 0, mx, my)
win.remove_color("basic")

win.refresh()
time.sleep(5)

win.exit()

