import chunk.string as string
from chunk.preprocessor import Preprocessor
import math

def shell_print(s):
    print("[SHELL] " + str(s))

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
    VAR_SCRIPT3     = Script(["COMMAND", "VAR_NAME", "CHUNK_NAME", "&:", "&:", "&:","CHUNK_VAR"])
    VAR_SCRIPT4     = Script(["COMMAND", "VAR_NAME", "CHUNK_NAME", "&:", "&:", "&:", "FUNCTION_NAME", "&:", "##ARGUMENTS"])
    VAR_SCRIPT5     = Script(["COMMAND", "VAR_NAME", "VAR1_NAME", "OPERATOR", "VAR2_NAME"])
    FUNCTION_CALL   = Script(["COMMAND", "FUNCTION_NAME", "&:", "##ARGUMENTS"])
    DEFINE_CHUNK    = Script(["COMMAND", "CHUNK_NAME", "&:", "&:"])
    DEFINE_FUNCTION = Script(["COMMAND", "FUNCTION_NAME", "&:", "&:","&:", "##ARGUMENTS"])
    RETURN_VALUE    = Script(["COMMAND", "RETURN_VALUE"])
    CHUNK_CALL      = Script(["COMMAND", "CHUNK_NAME", "&:", "&:", "&:", "FUNCTION_NAME", "&:", "##ARGUMENTS"])
    END             = Script(["COMMAND", "TARGET"])
    REASSIGN        = Script(["COMMAND", "VAR_NAME", "VAR_VALUE"])

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
            Visitor.GLOBAL_DEFINITIONS[line_data["CHUNK_NAME"]] = "CHUNK"
        if line_data["COMMAND"] in ("C", "CCAL"):
            Visitor.GLOBAL_DEFINITIONS[line_data["VAR_NAME"]] = "VARIABLE"
        if line_data["COMMAND"] == "D":
            Visitor.GLOBAL_DEFINITIONS[line_data["FUNCTION_NAME"]] = "FUNCTION"
        # if line_data["COMMAND"] == ">":
        #     Interpreter.GLOBAL_MEMORY[line_data["CHUNK_NAME"]] = "CHUNK"

        return line_data

    @staticmethod
    def error(s, n=-1):
        print("Scripter Error : line " + str(n) + ", " + s)

    @staticmethod
    def select_script(line, num=-1):

        if Script.check_front(line, "CCALL"):       return Scripter.apply_script(line, Scripts.VAR_SCRIPT2)
        if Script.check_front(line, "COP"):         return Scripter.apply_script(line, Scripts.VAR_SCRIPT5)
        if Script.check_front(line, "CHUNK"):       return Scripter.apply_script(line, Scripts.DEFINE_CHUNK)
        if Script.check_front(line, "CALL"):        return Scripter.apply_script(line, Scripts.FUNCTION_CALL)
        if Script.check_front(line, "C>>"):         return Scripter.apply_script(line, Scripts.VAR_SCRIPT4)
        if Script.check_front(line, "C>"):          return Scripter.apply_script(line, Scripts.VAR_SCRIPT3)
        if Script.check_front(line, "C"):           return Scripter.apply_script(line, Scripts.VAR_SCRIPT)
        if Script.check_front(line, "END"):         return Scripter.apply_script(line, Scripts.END)
        if Script.check_front(line, "D"):           return Scripter.apply_script(line, Scripts.DEFINE_FUNCTION)
        if Script.check_front(line, "RETURN"):      return Scripter.apply_script(line, Scripts.RETURN_VALUE)
        if Script.check_front(line, "R"):           return Scripter.apply_script(line, Scripts.REASSIGN)
        if Script.check_front(line, ">"):           return Scripter.apply_script(line, Scripts.CHUNK_CALL)

        Scripter.error("The given command is undefined.", num)
    

class Visitor():

    GLOBAL_MEMORY = {}
    GLOBAL_DEFINITIONS = {}

    # used to store argument values for functions
    TEMP_MEMORY = {}

    # used to change the way variables are put into memory depending on the scope
    CURRENT_SCOPE = ""
    CURRENT_FUNCTION = ""
    @staticmethod
    def parse(scripts, function_name=None):
        
        for command in scripts:

            # end command?
            if command["COMMAND"] == "END":
                Visitor.handle_end(command)

            if Visitor.CURRENT_FUNCTION != "":
                Visitor.GLOBAL_MEMORY[Visitor.CURRENT_FUNCTION][1].append(command)
                continue
                
            if command["COMMAND"] == "RETURN" and function_name != None:
                for key in Visitor.GLOBAL_MEMORY.keys():
                    if Visitor.GLOBAL_MEMORY[key] == function_name:
                        Visitor.GLOBAL_MEMORY[key] = Visitor.get_value(command["RETURN_VALUE"])

            if command["COMMAND"] == "R":
                Visitor.handle_reassign(command)


            # chunk function is being called
            if command["COMMAND"] == ">":
                if command["CHUNK_NAME"] == "root":
                    Visitor.handle_root_calls(command)
                else:
                    Visitor.handle_chunk_calls(command)
            
            # should we create a chunk
            if command["COMMAND"] == "CHUNK":
                Visitor.handle_chunk_creation(command)

            # variable is being created
            if command["COMMAND"] in ("C", "CCALL", "COP", "C>", "C>>"):
                Visitor.handle_assignments(command)

            if command["COMMAND"] == "D":
                Visitor.handle_function_creation(command)
            
            if command["COMMAND"] == "CALL":
                Visitor.handle_function_calls(command)
            
        print(Visitor.GLOBAL_MEMORY)

    @staticmethod
    def handle_root_calls(command):
        print("\nhandling root calls...")

        arg_values = []
        for a in command["##ARGUMENTS"]:
            arg_values.append(Visitor.get_value(a))
        
        if command["FUNCTION_NAME"] == "print":
            if len(arg_values) == 1:
                shell_print(arg_values[0])
            else:
                # arguments for print function are => "somestring %v"
                current_arg_index = 0
                text = ""

                for x in range(len(arg_values[0])):
                    char = arg_values[0][x]
                    # should a variable be placed here? => add next argument in list and skip this char
                    if char == "%" and x + 1 < len(arg_values[0]):
                        if arg_values[0][x+1] == "v":
                            current_arg_index += 1
                            text += str(arg_values[current_arg_index])
                            continue         
                    # is this "v" coming from a "%"? => ignore     
                    if char == "v" and x - 1 >= 0:
                        if arg_values[0][x-1] == "%":
                            continue
                    text += char
                
                shell_print(text)

    @staticmethod
    def handle_reassign(command):
        print("\nhandling reassign")

        var_name = command["VAR_NAME"]
        value = command["VAR_VALUE"]
        print(command)
        value_ = Visitor.get_value(value)

        Visitor.GLOBAL_MEMORY[Visitor.get_value(var_name)] = value_

    @staticmethod
    def handle_chunk_calls(command):
        print("\nhandling chunk call")
        
        chunk_name = command["CHUNK_NAME"]
        print("calling chunk : " + chunk_name)

        Visitor.handle_function_calls(command, chunk_name + "::")


    @staticmethod
    def handle_chunk_creation(command):
        print("\nhandling chunk creation")
        # adjusting scope
        Visitor.CURRENT_SCOPE = command["CHUNK_NAME"] + "::"
    
    @staticmethod
    def handle_function_creation(command):
        print("\nhandling function creation")
        
        func_name = command["FUNCTION_NAME"]
        func_args = command["##ARGUMENTS"]

        Visitor.CURRENT_FUNCTION = Visitor.CURRENT_SCOPE + func_name
        Visitor.GLOBAL_MEMORY[Visitor.CURRENT_FUNCTION] = [func_args, []]

        print("updated memory")
        print(Visitor.GLOBAL_MEMORY)

    @staticmethod
    def handle_function_calls(command, chunk_scope=""):
        print("\nhandling function calls")

        # extracting name
        func_name = command["FUNCTION_NAME"]
        func_name = chunk_scope + func_name

        for x in range(len(Visitor.GLOBAL_MEMORY[func_name][0])):
            # getting name of each argument
            arg = Visitor.GLOBAL_MEMORY[func_name][0][x]
            arg_ = Preprocessor.remove_front_whitespaces(arg)

            # getting the value for each argument
            given_arg = command["##ARGUMENTS"][x]
            given_arg_ = Preprocessor.remove_front_whitespaces(given_arg)

            # committing arg and corresponding value to global memory
            Visitor.GLOBAL_MEMORY[arg_] = Visitor.get_value(given_arg_)
        
        # calling function => simply parse all of the function lines
        Visitor.parse(Visitor.GLOBAL_MEMORY[func_name][1], func_name)



    @staticmethod
    def handle_end(command):
        print("\nhandling end statement")

        if command["TARGET"] == "D":
            Visitor.CURRENT_FUNCTION = ""
        if command["TARGET"] == "CHUNK" and "::" in Visitor.CURRENT_SCOPE:
            Visitor.CURRENT_SCOPE = ""

    @staticmethod
    def handle_assignments(command):
        print("\nhandling assignment")
        if command["COMMAND"] == "C":
            value = Visitor.get_value(command["VAR_VALUE"])
            if value != None:
                Visitor.GLOBAL_MEMORY[Visitor.CURRENT_SCOPE + command["VAR_NAME"]] = value 
                print("updated memory")
                print(Visitor.GLOBAL_MEMORY)

        elif command["COMMAND"] == "CCALL":
            print("return value assignment")

            # extracting function and variable name
            var_name = command["VAR_NAME"]
            func_name = command["FUNCTION_NAME"]

            # commiting to memory => might create temp_memory? (for safety) => do the same for args?
            Visitor.GLOBAL_MEMORY[var_name] = func_name

            # calling the fucntion => parser will handle return statements and loop through memory until it finds the correct function
            Visitor.handle_function_calls(command)

        elif command["COMMAND"] == "COP":
            print("operation assignment")
            var_name = command["VAR_NAME"]
            var_name1 = command["VAR1_NAME"]
            var_name2 = command["VAR2_NAME"]

            value_1 = Visitor.get_value(var_name1)
            value_2 = Visitor.get_value(var_name2)

            value_3 = None

            operation = command["OPERATOR"]
            if operation == "+":
                value_3 = value_1 + value_2
            elif operation == "-":
                value_3 = value_1 - value_2
            elif operation == "*":
                value_3 = value_1 * value_2
            elif operation == "/":
                value_3 = value_1 / value_2
            elif operation == "**" or operation == "pow":
                value_3 = value_1 ** value_2
            elif operation == "sqrt" or operation == "//":
                value_3 = round(value_1 ** (1 / value_2), 5)
        
            # commiting to memory
            Visitor.GLOBAL_MEMORY[var_name] = value_3
            print(value_3) 
        
        elif command["COMMAND"] == "C>":
            print("chunk variable assignment")
            chunk_name = command["CHUNK_NAME"]
            chunk_var_name = command["CHUNK_VAR"]
            var_name = command["VAR_NAME"]
            value = Visitor.get_value(chunk_name + "::" + chunk_var_name)
            if value != None:
                print("updating memory")
                Visitor.GLOBAL_MEMORY[var_name] = value
                print(Visitor.GLOBAL_MEMORY)
        
        elif command["COMMAND"] == "C>>":
            print("chunk call assignment")

            # extracting function and variable name
            var_name = command["VAR_NAME"]
            func_name = command["FUNCTION_NAME"]
            chunk_name = command["CHUNK_NAME"] + "::"
            func_name = chunk_name + func_name

            # commiting to memory => might create temp_memory? (for safety) => do the same for args?
            Visitor.GLOBAL_MEMORY[var_name] = func_name

            # calling the fucntion => parser will handle return statements and loop through memory until it finds the correct function
            Visitor.handle_function_calls(command, chunk_name)

            

    
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------

    @staticmethod
    def get_value(n):
        n_ = Preprocessor.remove_front_whitespaces(n)
        
        # checking if its a string:
        if n_[0] in ("'", '"') and n_[len(n_)-1] in ('"',"'"):
            return n_[1:len(n_)-1]

        # checking if bool
        if n_ == "false" or n_ == "true":
            return True if n_ == "true" else False
        
        # checking if in global memory
        if n_ in Visitor.GLOBAL_MEMORY.keys():
            return Visitor.GLOBAL_MEMORY[n_]

        # checking if it's a num
        try:
            num = float(n_)
            return num
        except:
            print("the given var is undefined")
            return None


