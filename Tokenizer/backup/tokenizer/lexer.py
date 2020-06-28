import tokenizer.string as string
from tokenizer.token import Token

class Lexer():

    @staticmethod
    def get_next_token(text, interpreter):
        """Should return the next token in the text, based on the current position of the interpreter."""
        if interpreter == None:Lexer.error()

        # the position of the interpreter could be out of bounds...
        try     :current_char = text[interpreter.pos]
        except  :return Token(Token.EOF, None)

        # is this character a digit?
        if current_char.isdigit():
            # getting the full number
            digit = Lexer.get_digit(text, interpreter.pos)
            interpreter.pos += len(digit)
            return Token(Token.NUMBER, digit)

        # is it an empty space
        if current_char == " ":
            interpreter.pos += 1
            return Token(Token.SPACE, " ")

        if current_char in ["+", "-", "/", "*"]:
            interpreter.pos += 1
            return Token(Token.symbol_token[current_char], current_char)

        if current_char == "(":
            interpreter.pos += 1
            return Token(Token.OPEN_BRACKETS, current_char)
        
        if current_char == ")":
            interpreter.pos += 1
            return Token(Token.CLOSED_BRACKETS, current_char)
        
        if current_char == '"':
            s,c = Lexer.get_string(text, interpreter.pos)
            interpreter.pos += len(s) + 2 + c
            return Token(Token.STRING, s)
        
        if current_char == "=":
            interpreter.pos += 1
            return Token(Token.ASSIGNMENT, current_char)
        
        if current_char == ",":
            interpreter.pos += 1
            return Token(Token.ARGUMENT_SEPARATOR, current_char)
        
        if current_char == ":":
            if interpreter.pos + 1 != len(text):
                if text[interpreter.pos + 1] == ":":
                    interpreter.pos += 2
                    return Token(Token.CALL, "::")
        
        interpreter.pos += 1
        return Token(Token.UNDEFINED, current_char)
    
    @staticmethod
    def get_digit(text, pos):
        found_digit = False
        current_pos = pos
        digit = ""
        digit_is_negative = False
        while found_digit == False:
            # if exceed the length, break
            if current_pos >= len(text):break

            # checking if this digit is negative
            # if current_pos > 0:
            #     if text[current_pos-1] == "-":
            #         if current_pos - 2 < 0:
            #             digit_is_negative = True
            #         if text[current_pos - 2] == " ":
            #             digit_is_negative = True
            #         if text[current_pos - 2] in ["+", "-", "/", "*"]:
            #             digit_is_negative = True 

            # is the current pos a digit?
            if text[current_pos].isdigit():
                digit += text[current_pos]
                current_pos += 1
                continue

            # are we at a dot (3.4) and was the previous number a digit?
            if text[current_pos] == "." and text[current_pos - 1].isdigit():
                digit += text[current_pos]
                current_pos += 1
                continue
            
            # if we get to this point it means that whatever we found ends here
            found_digit = True
        if digit_is_negative: digit = "-" + digit
        return digit 

    @staticmethod
    def get_string(text, pos):
        """Returns the string in the text starting at pos."""   
        found_string = ""
        in_string = False
        special_char_count = 0
        for x in range(len(text)):
            current_char = text[x]

            # are we in the string, entering the string or coming accros another quotation mark?
            if current_char == '"':
                if in_string:
                    if x > 0:
                        if text[x-1] == "$":
                            found_string += '"'
                            special_char_count += 1
                            continue
                    in_string = False
                else:
                    in_string = True
                continue

            if in_string and current_char != "$":
                found_string += current_char
            elif in_string and x > 0 and text[x-1] == "$" and current_char == "$":
                special_char_count += 1
                found_string += current_char
            
        return '"' + found_string + '"', special_char_count

    @staticmethod
    def error():
        raise Exception("No interpreter given.")

    

class Parser():

    # contains all of the variables created by the user.
    GLOBAL_MEMORY = {}
    DEBUG = True

    @staticmethod
    def parse(tokens):
        """Looks for specific keywords in the given tokens and returns value/command."""
        result = []

        # looking for assignments
        if Token.includes(tokens, Token.ASSIGNMENT):
            log("Found assignment")
            Parser.handle_assignment(tokens)

        # is this a pure opoertaion:
        if Parser.is_operation(tokens):
            log("Found operation")
            return Parser.handle_operation(tokens)

        return result
    
    @staticmethod
    def handle_assignment(tokens):
        """Extracts the values out of the given assignment tokens."""
        
        key_tokens = []
        value_tokens = []

        append_keys = True
        for t in tokens:
            if t.type == Token.ASSIGNMENT:
                append_keys = False
            elif append_keys:key_tokens.append(t)
            else:value_tokens.append(t)
        
        # check if value tokens are an operation!

        key = Token.smash(key_tokens)
        value = Token.smash(value_tokens)

        # key cannnot be empty
        if string.isempty(key):
            Parser.InvalidKey()

        log("Found : " + key + " and " + value)
        # checking the data type 
            # for value : 
            # => is it a string?
            # => is it a boolean?
            # => does it refer back to an already declared variable?
            # => can we convert it to a number?
            # => raise Error
        if '"' in value:value = value[1:len(value)-1]
        elif value == "false": value = False
        elif value == "true" : value = True
        else:
            if value in Parser.GLOBAL_MEMORY.keys():
                value = Parser.GLOBAL_MEMORY[value]
            else:
                try:
                    value = float(value)
                except:
                    Parser.UnknowDataType(key)
                    return

        # committing to memory
        Parser.GLOBAL_MEMORY[key] = value

    @staticmethod
    def handle_operation(tokens, r=True):
        """Handles multiplication, division, addition, ..... """
        result = 0

        left_tokens = []
        right_tokens = []
        sign_tokens = []

        is_left = True
        in_brackets = False 

        for t in tokens:
            if t.type == Token.OPEN_BRACKETS and not in_brackets:
                in_brackets = True
                continue
            if t.type == Token.CLOSED_BRACKETS and in_brackets:
                in_brackets = False
                continue

            if t.value in ["+", "*", "-", "/"] and is_left and not in_brackets:
                sign_tokens.append(t)
                is_left = False
                continue
                
            if is_left:left_tokens.append(t)
            else:right_tokens.append(t)
        
        print("\nleft")
        for t in left_tokens:print(str(t))
        print("right")
        for t in right_tokens:print(str(t))
        print("sign")
        for t in sign_tokens:print(str(t))
        
        # if len(left_tokens) == 1 and len(right_tokens) == 0:
        #     return int(left_tokens[0].value)
        # if len(left_tokens) == 0 and len(right_tokens) == 1:
        #     return int(right_tokens[0].value)
        
        

        return result

    @staticmethod
    def is_operation(tokens):
        if Token.includes(tokens, Token.ADD) or Token.includes(tokens, Token.SUB) or Token.includes(tokens, Token.DIV) or Token.includes(tokens, Token.MUL):
            return True
        return False

    # ---------------------------------------------------------------------------------
    #       ERRORS
    # ---------------------------------------------------------------------------------

    @staticmethod
    def UnknowDataType(key):
        raise Exception("The given value for the variable '" + key + "' is undefined.")
    
    @staticmethod
    def InvalidKey():
        raise Exception("The given key is invalid.")

def log(s):
    if Parser.DEBUG:print(str(s))