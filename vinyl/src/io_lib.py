"""
Contains functions for writing and reading data to files.
"""
import os, sys
try:
    import shutil
except:
    print("[Import-Error] Couldn't import the module 'shutil', multiple functions related to files will not work.")

def write_dictionary(dic, path, separator="=", appendmode="w"):
    """Writes the given dictionary to the given path. The default separator between each key and value is '='."""
    # getting the keys
    ks = dic.keys()

    # opening the file and writing
    f = open(path, appendmode)
    i = 0
    for k in ks:
        f.write(str(k) + separator + str(dic[k]) + ("" if i == len(ks) - 1 else "\n"))
        i+=1
    f.close()

def read_dictionary(path, separator="="):
    """Reads the file at the path and construct a dictionary out of it."""
    f = open(path, "r")
    dic = {}
    for line in f:
        
        key = ""
        value = ""
        found = False
        for char in line:
            if found: value += char
            if char == separator:found = True
            if not found:key += char
        
        dic[key] = value.rstrip("\n")
            
    f.close()
    return dic

def reverse_dictionary(dict):
    ks = list(dict.keys())
    vs = list(dict.values())

    new_dict = {}
    for x in range(len(vs)):
        new_dict[vs[x]] = ks[x]
    return new_dict

def read_file(path):
    """Reads the file at the given path and returns all the lines in an array."""
    lines = []
    f = open(path, "r")
    for line in f:
        lines.append(line.rstrip("\n"))
    f.close()
    return lines

def error_using_():
    print("[Error] Function not completed.")

def createFile(path):
    try:
        f = open(path, "a")
        f.close()
        return 0
    except:
        error_using_()
        return 1

def createFolder(path):
    try:
        os.mkdir(path)
        return 0
    except:
        error_using_()
        return 1

def removeFile(path):
    try:
        os.remove(path)
        return 0
    except:
        error_using_()
        return 1
    
def removeFolder(path):
    try:
        shutil.rmtree(path)
        return 0
    except:
        error_using_()
        return 1
    
def movePath(src, dst):
    try:
        shutil.move(src, dst)
        return 0
    except:
        error_using_()
        return 1 

def copyFolder(src, dst):
    try:
        shutil.copytree(src, dst)
        return 0
    except:
        error_using_()
        return 1

def copyFile(src, dst):
    try:
        shutil.copyfile(src, dst)
        return 0
    except:
        error_using_()
        return 1