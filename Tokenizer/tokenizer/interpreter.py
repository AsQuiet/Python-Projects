from tokenizer.lexer import Lexer, Parser

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
        # print(Parser.parse(tokens))
        