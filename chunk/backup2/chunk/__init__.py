from chunk.preprocessor import Preprocessor
from chunk.lexer import Lexer
from chunk.parser import Parser

def run(path):
    # print("running chunk file at : " + path)

    # put file through the preprocessor
    lines = Preprocessor.process(path)

    # running
    i = Interpreter()
    i.interpret(lines)

class Interpreter():

    def __init__(self):
        self.GLOBAL_MEMORY = {}
    
    def interpret(self, lines):
        tokens = []
        i = 0
        for line in lines:
            i += 1
            ts = Lexer.get_tokens(line, i)
            tokens.append(ts)
        
        print("\nparsing commands :")
        commands = []
        for line_tokens in tokens:
            commands.extend(Parser.parse_line(line_tokens))
        print(" ")
        print(str(commands))

