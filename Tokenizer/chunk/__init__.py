from chunk.preprocessor import Preprocessor
from chunk.lexer import Lexer

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
        for line in lines:
            ts = Lexer.get_tokens(line)
            tokens.extend(ts)
            
        for t in tokens:print(str(t))
