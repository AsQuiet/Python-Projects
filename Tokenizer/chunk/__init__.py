from chunk.preprocessor import Preprocessor
from chunk.interpreter import Interpreter
from chunk.scripter import Script, Scripter

def run(path):
    
    lines = Preprocessor.process(path)

    # getting the commands from scripter (lexer)
    commands = []
    num = 0
    for line in lines:
        num += 1
        commands.append(Scripter.select_script(line, num))
    
    print("\nparsed commands :")
    for c in commands:
        print("     "+str(c))
    print("---") 
    print(Interpreter.GLOBAL_DEFINITIONS)

    Interpreter.parse(commands)
           