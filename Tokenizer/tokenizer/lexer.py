import tokenizer.string as string
import tokenizer.token as tok

class Lexer():

    @staticmethod
    def get_next_token(text, interpreter):
        """Should return the next token in the text, based on the current position of the interpreter."""
        if interpreter == None:Lexer.error();

        # the position of the interpreter could be out of bounds...
        try     :current_char = text[interpreter.pos]
        except  :return tok.Token(tok.Token.EOF, None)

        # is this character a digit?
        if current_char.isdigit():
            # getting the full number
            digit = Lexer.get_digit(text, interpreter.pos)
            interpreter.pos += len(digit)
            return tok.Token(tok.Token.NUMBER, digit)

        # is it an empty space
        if current_char == " ":
            interpreter.pos += 1
            return tok.Token(tok.Token.SPACE, " ")

        if current_char in ["+", "-", "/", "*"]:
            interpreter.pos += 1
            return tok.Token(tok.Token.symbol_token[current_char], current_char)

        if current_char == "(":
            interpreter.pos += 1
            return tok.Token(tok.Token.OPEN_BRACKETS, current_char)
        
        if current_char == ")":
            interpreter.pos += 1
            return tok.Token(tok.Token.CLOSED_BRACKETS, current_char)
        
        if current_char == '"':
            s,c = Lexer.get_string(text, interpreter.pos)
            interpreter.pos += len(s) + 2 + c
            return tok.Token(tok.Token.STRING, s)
        
        if current_char == "=":
            interpreter.pos += 1
            return tok.Token(tok.Token.ASSIGNMENT, current_char)
        
        if current_char == ",":
            interpreter.pos += 1
            return tok.Token(tok.Token.ARGUMENT_SEPARATOR, current_char)
        
        if current_char == ":":
            if interpreter.pos + 1 != len(text):
                if text[interpreter.pos + 1] == ":":
                    interpreter.pos += 2
                    return tok.Token(tok.Token.CALL, "::")
        
        interpreter.pos += 1
        return tok.Token(tok.Token.UNDEFINED, current_char)
    
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
            
            
            
            

        return found_string, special_char_count

    @staticmethod
    def error():
        raise Exception("No interpreter given.")

    

class Parser():

    @staticmethod
    def parse(tokens):
        result = []

        for x in range(len(tokens)):
            token = tokens[x]
            print("handling token : " + str(token))

            if token.type == tok.Token.NUMBER:
                operation = tokens[x + 1].type
                result.extend([operation, token.value])


        return result