import sys, os

# query path tag1 tag2 tag3 -r
# -r => read files as well

def main():

    # getting the path, tags and mode (-r of none)
    try: 
        path = sys.argv[1]
        if not os.path.exists(path):path = None
    except: path = None
    if path == None:
        print("The given path does not exist.")
        return

    # getting all the tags
    tags = get_tags(sys.argv)
    if tags == None:
        print("The given tags don't exists or are invalid.")
        return

    results = query(path, tags)
    print_table(results)

def handle_ignore():

    if "clear" in sys.argv:ignore.clear()
    if "print" in sys.argv:print(ignore)

    if 'add' in sys.argv:ignore.extend(get_flags("add", sys.argv))

    if "remove" in sys.argv: 
        to_remove = get_flags("remove", sys.argv)
        for r in to_remove:
            if r in ignore:
                ignore.remove(r)

    write_array_to_file(arr=ignore)
    pass

def query(path, tags, cs_path=""):

    # the files in this dir => that we want to check
    files = os.listdir(path)

    # wich files or folders match the tags
    results = []
    
    for file in files:

        # should we ignore the file
        if file in ignore:continue

        newPath = os.path.join(path, file)
        isdir = os.path.isdir(newPath)

        tag_in, found_tag = path_contains_tags(file, tags)
        if tag_in:results.append({"path" : cs_path + "/" + file, "found tag" : found_tag })

        # recursion
        if isdir:results.extend(query(newPath, tags, cs_path + "/" + file))

    return results

def path_contains_tags(path, tags):
    for tag in tags:
        if tag in path:
            return True, tag
    return False, None

def get_file_as_array(path="./query_ignore.txt"):
    f = open(path, "r")
    lines = []
    for line in f:lines.append(line.rstrip("\n"))
    f.close()
    return lines

def write_array_to_file(path="./query_ignore.txt",arr=[]):
    f = open(path, "w")
    for line in arr:f.write(line + "\n")
    f.close()

def get_tags(args):
    tags = args[2:len(args)]
    return tags

def get_flags(key, args):
    flags = []
    if key in args:
        flags = args[args.index(key) + 1:len(args)]
    return flags        

def print_table(data):
    table = ""

    center_col_width = 0

    # finding the longest coll
    for d in data:
        if len(d["path"]) > center_col_width:
            center_col_width = len(d["path"]) + 5

    for x in range(len(data)):
        d = data[x]
        # indices
        table += str(x) + gen_empty(4 - len(str(x))) + " | "

        # paths
        table += d["path"] + gen_empty( center_col_width - len(d["path"])) + " | "

        # found tag
        table += d["found tag"]

        table += "\n"
    print(table)

def gen_empty(n=50):
    s = ""
    for x in range(n):s+=" "
    return s


ignore = get_file_as_array()
if __name__ == "__main__":
    if "__ignore__" in sys.argv:handle_ignore()
    else: main()

