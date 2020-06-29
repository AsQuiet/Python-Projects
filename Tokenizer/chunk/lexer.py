from chunk.string import remove_characters
from chunk.token import Token, TokenTypes

class Lexer():

    @staticmethod
    def get_tokens(line):
        print("lexing line : " + line)
        current_pos = 0
        tokens = []

        if Lexer.is_line_keyword("end", remove_characters(line, [" "])):
            return [Token(TokenTypes.END, "end")] 
            
        if Lexer.is_line_keyword("return", line):
            tokens.append(Token(TokenTypes.RETURN, "return"))
            current_pos += len("return")

        while True:
            if current_pos >= len(line):break

            current_char = line[current_pos]
            current_pos += 1

            if current_char == '"':
                s, new_pos = Lexer.get_string(line,current_pos-1)
                tokens.append(Token(TokenTypes.STRING, s))
                current_pos = new_pos
                continue

            if current_char.isdigit():
                digit, new_pos = Lexer.get_digit(line, current_pos - 1)
                current_pos = new_pos
                tokens.append(Token(TokenTypes.NUM,digit))
                continue

            if current_char == "=":
                tokens.append(Token(TokenTypes.ASSIGNMENT, "="))
                continue
            
            if current_char == ">":
                if current_pos < len(line):
                    if line[current_pos] == ">":
                        tokens.append(Token(TokenTypes.CREATE_CHUNK, ">>"))
                        current_pos += 1
                        continue
                tokens.append(Token(TokenTypes.CHUNK_POINTER, ">"))
                continue

            # looking for operations
            if current_char in ("+", "-", "/", "*"):
                if current_char == "+":tokens.append(Token(TokenTypes.ADD, current_char))
                if current_char == "-":tokens.append(Token(TokenTypes.SUB, current_char))
                if current_char == "/":tokens.append(Token(TokenTypes.DIV, current_char))
                if current_char == "*":tokens.append(Token(TokenTypes.MUL, current_char))
                continue
                
            if current_char == "(":
                tokens.append(Token(TokenTypes.OPEN_PAREN, "("))
                continue
                
            if current_char == ")":
                tokens.append(Token(TokenTypes.CLOSE_PAREN, ")"))
                continue

            # checking for arrays
            if current_char == "[":
                tokens.append(Token(TokenTypes.OPEN_ARR, "["))
                continue
            
            if current_char == "]":
                tokens.append(Token(TokenTypes.CLOSE_ARR, "]"))
                continue
            
            # arguments and function call / definitions
            if current_char == ",":
                tokens.append(Token(TokenTypes.ARG_SEPARATOR, ","))
                continue
            
            # double dot can be create function or call function
            if current_char == ":":
                if current_pos < len(line):
                    if line[current_pos] == ":":
                        tokens.append(Token(TokenTypes.CREATE_FUNCTION, "::"))
                        current_pos += 1
                        continue
                tokens.append(Token(TokenTypes.CALL_FUNCTION, ":"))
                continue
            
            # ingnore empty whitespace
            if current_char == " ":
                # tokens.append(Token(TokenTypes.EMPTY, " "))
                continue

            tokens.append(Token(TokenTypes.UNDEFINED, current_char))


        return tokens
    
    @staticmethod
    def get_digit(text, pos):
        found_digit = False
        current_pos = pos
        digit = ""
        digit_is_negative = False
        while found_digit == False:
            # if exceed the length, break
            if current_pos >= len(text):break

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
        return digit, current_pos
        
    @staticmethod
    def get_string(text, pos):
        """Returns the string in the text starting at pos."""   
        current_pos = pos
        found_string = ""
        in_string = False
        
        while True:
            if current_pos >= len(text):break;
            current_char = text[current_pos]

            if current_char == '"':
                # the user might want to type a ", then the user should use a $ before 
                if current_pos > 0:
                    if text[current_pos - 1] == "$":
                        found_string += '"'
                        current_pos += 1
                        continue
                in_string = not in_string
            
            if in_string and current_char != "$": 
                found_string += current_char
                current_pos += 1
            
            if in_string and current_char == "$":
                if current_pos > 0:
                    if text[current_pos - 1] == "$":
                        found_string += "$"
                current_pos += 1

            if not in_string:break
            

        return found_string+'"',current_pos + 1
    
    @staticmethod
    def is_line_keyword(keyword, line):
        if len(keyword) <= len(line):
            for x in range(len(keyword)):
                if keyword[x] != line[x]:
                    return False
            return True
        return False