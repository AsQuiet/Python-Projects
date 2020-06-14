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

    pass


# base64 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "+"]


    

