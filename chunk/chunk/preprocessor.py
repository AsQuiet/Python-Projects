"""Clears out file and makes it ready to be interpreted.
i.e. removes comments, includes other files, removes whitespaces, ..."""

import os, chunk.string as string

class Preprocessor():

    @staticmethod
    def process(path):
        if not os.path.exists(path): return
        lines = []
        f = open(path, "r")
        in_comment_section = False
        for line in f:
            line = line.rstrip("\n")
            if string.isempty(line): continue
            if len(line) > 2:
                if line[0] == "/" and line[1] == "/":
                    continue
            if "/*" in line:
                in_comment_section = True
                continue
            if "*/" in line and in_comment_section:
                in_comment_section = False
                continue
            if in_comment_section:continue
            lines.append(Preprocessor.remove_front_whitespaces(line))
            
        f.close()
        return lines
    
    @staticmethod
    def remove_front_whitespaces(line):
        """  eg:
        CHUNK l
            D ll::
            END
        END
        
        gets converted to

        CHUNK l
        D ll::
        END
        END
        """
        is_em = True
        line_ = ""
        for char in line:
            if char != " " and is_em:
                is_em = False
            if not is_em:
                line_ += char
        return line_
