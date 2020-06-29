import chunk.string as string
import chunk.interpreter as itpr

class Script():
    def __init__(self, script_arr):
        self.script_arr = script_arr
    
    @staticmethod
    def split(line):
        arr = []

        current_value = ""

        # for string tokenazation
        in_string = False

        for x in range(len(line)):
            char = line[x]

            if char == " " and not string.isempty(current_value) and not in_string:
                arr.append(current_value)
                current_value = ""
                continue  
            
            # checking for special characters '$'
            if x > 0 and (char == "'" or char == "'"):
                if line[x - 1] == "$":
                    current_value += char
                    continue
            
            if char == "$":
                if line[x - 1] == "$":
                    current_value += char
                    continue
                continue

            if char == '"' or char == "'":
                if in_string:in_string = False
                else: in_string = True

            # checking for other tokens
            if char == ":" and not in_string:
                arr.append(current_value)
                current_value = ""
                arr.append(char)
                continue

            if char == "," and not in_string:
                arr.append(current_value)
                current_value = ""
                continue

            current_value += char

        if not string.isempty(current_value):arr.append(current_value)

        return arr 
    
    @staticmethod
    def check_front(line, n):
        if len(line) < len(n):return False
        for x in range(len(n)):
            if n[x].lower() != line[x].lower():
                return False
        return True 

# ------------------------------------------------------------------------------------------
#       ---SCRIPTER---
# ------------------------------------------------------------------------------------------

class Scripts():
    VAR_SCRIPT      = Script(["COMMAND", "VAR_NAME", "VAR_VALUE"])
    VAR_SCRIPT2     = Script(["COMMAND", "VAR_NAME", "FUNCTION_NAME", "&:", "##ARGUMENTS"])
    FUNCTION_CALL   = Script(["COMMAND", "FUNCTION_NAME", "&:", "##ARGUMENTS"])
    DEFINE_CHUNK    = Script(["COMMAND", "CHUNK_NAME", "&:", "&:"])
    DEFINE_FUNCTION = Script(["COMMAND", "FUNCTION_NAME", "&:", "&:","&:", "##ARGUMENTS"])
    RETURN_VALUE    = Script(["COMMAND", "RETURN_VALUE"])
    CHUNK_CALL      = Script(["COMMAND", "CHUNK_NAME", "&:", "&:", "&:", "FUNCTION_NAME", "&:", "##ARGUMENTS"])

class Scripter():

    @staticmethod
    def apply_script(line, script):
        line_data = {}
        line_keywords = Script.split(line)

        for x in range(len(script.script_arr)):
            script_key = script.script_arr[x]

            if script_key in ("VAR_NAME", "FUNCTION_NAME"):
                line_keywords[x] = string.remove_characters(line_keywords[x], [" "])

            # stands for symbol
            if "&" in script_key:continue
            # means that all following data should be put in an array
            if "##" in script_key:
                arr = []
                i = x
                while True:
                    try:
                        arr.append(line_keywords[i])
                    except:
                        break
                    i += 1
                line_data[script_key] = arr
                break

            # general rule
            line_data[script_key] = line_keywords[x]
            if script_key == "COMMAND":
                line_data[script_key] = line_keywords[x].upper()

        if line_data["COMMAND"] == "CHUNK":
            itpr.Interpreter.GLOBAL_DEFINITIONS[line_data["CHUNK_NAME"]] = "CHUNK"
        if line_data["COMMAND"] in ("C", "CCAL"):
            itpr.Interpreter.GLOBAL_DEFINITIONS[line_data["VAR_NAME"]] = "VARIABLE"
        if line_data["COMMAND"] == "D":
            itpr.Interpreter.GLOBAL_DEFINITIONS[line_data["FUNCTION_NAME"]] = "FUNCTION"
        # if line_data["COMMAND"] == ">":
        #     Interpreter.GLOBAL_MEMORY[line_data["CHUNK_NAME"]] = "CHUNK"

        return line_data

    @staticmethod
    def error(s, n=-1):
        print("Scripter Error : line " + str(n) + ", " + s)

    @staticmethod
    def select_script(line, num=-1):
        if Script.check_front(line, "CCALL"):return Scripter.apply_script(line, Scripts.VAR_SCRIPT2)
        if Script.check_front(line, "CHUNK"):return Scripter.apply_script(line, Scripts.DEFINE_CHUNK)
        if Script.check_front(line, "CALL"):return Scripter.apply_script(line, Scripts.FUNCTION_CALL)
        if Script.check_front(line, "C"):return Scripter.apply_script(line, Scripts.VAR_SCRIPT)
        if Script.check_front(line, "END"):return {"COMMAND":"END"}
        if Script.check_front(line, "D"):return Scripter.apply_script(line, Scripts.DEFINE_FUNCTION)
        if Script.check_front(line, "RETURN"):return Scripter.apply_script(line, Scripts.RETURN_VALUE)
        if Script.check_front(line, ">"):return Scripter.apply_script(line, Scripts.CHUNK_CALL)

        Scripter.error("The given command is undefined.", num)
    
        