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
            if current_pos == len(line):break
            current_char = line[current_pos]
            current_pos += 1

            if current_char == '"':
                s, c = Lexer.get_string(line)
                tokens.append(Token(TokenTypes.STRING, s))
                current_pos += len(s) - 1 + c
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
    def get_string(text):
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
    def is_line_keyword(keyword, line):
        if len(keyword) <= len(line):
            for x in range(len(keyword)):
                if keyword[x] != line[x]:
                    return False
            return True
        return False