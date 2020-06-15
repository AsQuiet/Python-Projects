import math

def reverse(a):
    new_array = []
    for x in range(len(a)):
        new_array.append(a[len(a) - x - 1])
    return new_array

def arrayToString(a):
    s = ""
    for x in range(len(a)):
        s += str(a[x]) 
    return s

def stringToArray(s, func=None):
    arr = [] 
    for x in range(len(s)):
        arr.append(s[x] if func == None else func(s[x]))
    return arr

def gen_buffer(length):
    if length <= 0:return ""
    s = ""
    for x in range(length):
        s += "0"
    return s

def mod_int(n, d=2):
    i = int(n / d)
    m =n % d
    return [i, m]

# ------------------------------------------------------------
#   USER FUNCTIONS
# ------------------------------------------------------------

def convert_int(n, length=None):
    """
    Converts the given integer to a binary number (string).
    """
    if n == 0: return ("0" if length == None else gen_buffer(length))
    current = n
    b = []
    while current > 0:
        re = mod_int(current)
        b.append(str(re[1]))
        current = re[0]
    result = arrayToString(reverse(b))

    # adding some buffer space if needed
    result = result if length == None else gen_buffer(length - len(result)) + result

    return result

def convert_binary_int(b):
    """
    Converts the given binary number (string) to an integer.
    """
    total = 0
    for x in range(len(b)):
        total = 2 * total + int(b[x])
    
    return total

def convert_decimal(n, precision=20):
    """
    Converts the given decimal to a binary number with the given precision.
    """
    # converting fractional part
    current = n if n < 1 else n - int(n)
    result = ""

    for x in range(precision):
        next_int = int(current * 2)
        next_ = current * 2 - next_int

        result += str(next_int)
        if next_ == 0: 
            break
        current = next_

    # converting integer part
    i = "0." if int(n) < 1 else convert_int(int(n)) + "."

    return i + result

def convert_binary_decimal(b):
    """
    Converts the given binary string to a decimal.
    """
    # getting the fractional part
    decimal = b[b.index(".")+1:len(b)]

    # reversing the string
    decimal = arrayToString(reverse(stringToArray(decimal)))

    current = 0
    for x in range(len(decimal)):
        # getting integer part
        i = int(decimal[x])
        # getting the next current
        next_ = 0.5 * (i + current)
        # print("1/2 * (" + str(i) + " + " + str(current) + ") = " + str(next_))

        current = next_
    
    # converting the integer part
    i = b[0:b.index(".")]
    i = 0 if len(i) == 0 else convert_binary_int(i)
    
    return current + i

# ---------------------------------------------------------------------------------------------------
# IO [FILES]
# ---------------------------------------------------------------------------------------------------

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
        dic[String.remove_characters_from_char(line, "=")] = String.remove_characters_from(line, 0, line.index("=") + 1).rstrip("\n")
    f.close()
    return dic

def reverse_dictionary(dict):
    ks = list(dict.keys())
    vs = list(dict.values())

    new_dict = {}
    for x in range(len(vs)):
        new_dict[vs[x]] = ks[x]
    return new_dict

# ---------------------------------------------------------------------------------------------------
# STRING []
# ---------------------------------------------------------------------------------------------------

class String:
    """Very basic string manipulation functions."""

    @staticmethod
    def toArray(stri):
        """Converts the given string into an array of strings."""
        a = []
        for x in range(len(stri)):
            a.append(stri[x])
        return a
    
    @staticmethod
    def fromArray(arr, separator=""):
        """Creates a string from the given array."""
        string = ""
        for el in arr:string += str(el) + separator
        return string

    @staticmethod
    def toRange(stri):
        """Returns the range object for this string."""
        return range(len(stri))

    @staticmethod
    def remove_characters(stri, chars):
        """Removes all the given characters from the given string."""
        new_str = ""
        for char in String.toArray(stri):
            if not char in chars:new_str += char          
        return new_str

    @staticmethod
    def remove_characters_from(stri, start, end):
        """Removes all the characters of a string starting at 'start' and ending at 'end' (indices). Start is included and end is excluded."""   
        end = len(stri) if end == None else end
        new_str = ""
        for x in String.toRange(stri):
            if x < start or x >= end:new_str += stri[x]
        return new_str
    
    @staticmethod
    def remove_characters_from_char(stri, start, end=None):
        """Removes all the characters of a string between the characters 'start' and 'end'. Start is included and end is excluded."""
        new_str = ""
        add_c = True
        for x in String.toRange(stri):
            if stri[x] == start:add_c = False
            if stri[x] == end  :add_c = True
            if add_c:new_str += stri[x]
        return new_str
    
    @staticmethod
    def list_separator(stri, separator="-"):
        """eg: list_separator('2020-06-13', '-') => [2020,06,13] """
        current_string = ""
        arr = []

        for char in String.toArray(stri):
            if char == separator:
                arr.append(current_string)
                current_string = ""
            else: current_string += char
        arr.append(current_string.rstrip("\n"))
        return arr

    @staticmethod
    def reverse(stri):
        """Reverses the given string."""
        string_array = String.toArray(stri)
        string_array.reverse()
        return String.fromArray(string_array)
    
    @staticmethod
    def remove_index(stri, indices=[0]):
        """Removes the given indeces from the string."""
        new_string = ""
        for x in String.toRange(stri):
            if not x in indices:new_string+=stri[x]
        return new_string
    
    @staticmethod
    def remove_last(stri):
        """Removes the last element from the given string."""
        return String.remove_index(stri, [len(stri)-1])

    @staticmethod
    def remove_first(stri):
        """Removes the first element from the given string."""
        return String.remove_index(stri,0)

    @staticmethod
    def get_last_index(stri):
        """Returns the index of the last element of the string."""
        return len(stri) - 1
    
    @staticmethod
    def map_string(stri, func):
        """Constructs a new string from the original string called the function. The function should have as its arguments the character and the index."""
        new_string = ""
        for x in String.toRange(stri):
            char = stri[x]
            new_string += func(char, x)
        return new_string

