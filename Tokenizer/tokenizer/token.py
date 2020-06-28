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
        # integers or +, - or None if EOF
        self.value = value
    
    def __str__(self):
        return "Token(" + self.type + ", " + str(self.value) + ")"

    def __eq__(self, other):
        return (self.type, self.value) == (other.type, other.value)
    
    