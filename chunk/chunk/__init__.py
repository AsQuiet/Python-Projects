from chunk.preprocessor import Preprocessor
from chunk.scripter import Script, Scripter, Visitor

def run(path):
    
    lines = Preprocessor.process(path)

    Visitor.GLOBAL_MEMORY = {}
    Visitor.GLOBAL_DEFINITIONS = {}
    Visitor.CURRENT_SCOPE = ""
    Visitor.CURRENT_FUNCTION = ""

    # getting the commands from scripter (lexer)
    commands = []
    num = 0
    for line in lines:
        num +=  1
        s = Scripter.select_script(line, num)
        if s != None:
            commands.append(s)
    
    # print("\nparsed commands :")
    # for c in commands:
    #     print("     "+str(c))
    # print("---") 

    # print("global definitions : " + str(Visitor.GLOBAL_DEFINITIONS) + "\n\n")

    Visitor.parse(commands)
           