class TokenTypes():
    ADD = "ADD"
    SUB = "SUB"
    DIV = "DIV"
    MUL = "MUL"
    NUM = "NUM"
    STRING = "STRING"
    OPEN_PAREN = "OPEN_PAREN"
    CLOSE_PAREN = "CLOSE_PAREN"
    OPEN_ARR = "OPEN_ARR"
    CLOSE_ARR = "CLOSE_ARR"

    CALL_FUNCTION = "CALL"
    CREATE_FUNCTION = "CREATE_FUNCTION"
    CHUNK_POINTER = "CHUNK_POINTER"
    ARG_SEPARATOR = "ARG_SEPARATOR"

    EMPTY = "EMPTY"
    EOF = "EOF"
    UNDEFINED = "UNDEFINED"

    # keywords
    END = "END"
    CREATE_CHUNK = "CREATE_CHUNK"
    RETURN = "RETURN"
    # operators
    ASSIGNMENT = "ASSIGNMENT"  # = 


class Token():

    def __init__(self, type=TokenTypes.EOF, value=None):
        self.type = type
        self.value = value
    
    def __str__(self):
        return "Token(" + self.type + ", " + str(self.value) + ")"