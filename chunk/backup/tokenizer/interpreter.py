from tokenizer.lexer import Lexer, Parser, string
from tokenizer.token import Token

import os

class Interpreter():

    def __init__(self):
        # will be analyzd through the lexer
        self.text = ""
        # position in the text
        self.pos = 0

    def error(self):
        raise Exception("Error parsing the input...")

    def set_text(self, text):
        self.text = text
        self.pos = 0
    
    def run(self):

        tokens = []
        # reading the line
        i = 0
        while True:
            token = Lexer.get_next_token(self.text, self)   
            if token.type == "EOF":break
            if token.type != "SPACE":tokens.append(token)
            i += 1
            if i > 100: break
        
        for t in tokens:print(str(t))
        print(Parser.parse(tokens))
        print(Parser.GLOBAL_MEMORY)
    
    def read_file(self,path):
        if not os.path.exists(path):raise Exception("Given path does not exists.")

        f = open(path, "r")
        incomment = False
        for line in f:
            if string.isempty(line.rstrip("\n")):continue
            if "//" in line : continue
            if "/*" in line: 
                incomment = True
                continue
            if "*/" in line:
                incomment = False
                continue
            if incomment:continue
            self.set_text(line.rstrip("\n"))
            self.run()
        f.close()
        print("File Is Done")