class Token():

    ADD = "ADD"
    EOF = "EOF"
    SUB = "SUB"
    SPACE = "SPACE"
    INT = "INT"
    FLOAT = "FLOAT"
    NUMBER = "NUMBER"
    DIV = "DIV"
    MUL = "MUL"
    OPEN_BRACKETS = "OPEN_BRACKETS, ("
    CLOSED_BRACKETS = "CLOSED_BRACKETS, )"
    STRING = "STRING"
    UNDEFINED = "UNDEFINED"
    ASSIGNMENT = "ASSIGNMENT"
    CALL = "CALL"
    ARGUMENT_SEPARATOR = "ARGUMENT_SEPARATOR"
    

    symbol_token = {
        "+" : ADD,
        "-" : SUB,
        "/" : DIV,
        "*" : MUL
    }

    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    def __str__(self):
        return "Token(" + self.type + ", " + str(self.value) + ")"

    def __eq__(self, other):
        return (self.type, self.value) == (other.type, other.value)
    
    @staticmethod
    def smash(tokens):
        """Smashes together all of the tokens' values to create a string from them."""
        s = ""
        for t in tokens: s+=t.value if t.value != None else ""
        return s
    
    @staticmethod
    def find_all_type(tokens, type):
        ts = [] 
        for t in tokens:
            if t.type == type:
                ts.append(t)
        return ts

    @staticmethod
    def find_type(tokens, type):
        for t in tokens:
            if t.type == type:
                return t
        return None

    @staticmethod
    def includes(tokens, type):
        ts = Token.find_all_type(tokens, type)
        if len(ts) == 0:return False
        return True
    