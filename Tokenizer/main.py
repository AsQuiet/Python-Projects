from tokenizer import Interpreter

shell = Interpreter()

eq = 'print::34, 34'
shell.set_text(eq)
shell.run()

