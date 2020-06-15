import briefio

alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
msc = {
    "\n":"[a]",
    "=":"[b]",
    " ":"[][]]][][${[{[}}{}["
}

msc_ = briefio.reverse_dictionary(msc)

def convert_bin_scramble(path, key=[0,0,0,0,0,0]):

    f = open(path, "r")
    b = open("converted.bin", "w")

    def add_key(char, index):
        return str( int(char) + key[index])

    for line in f:
        line = line.rstrip("\n")
        bin_chars = []
        for char in line:
            if char in alp:
                # generating the bin
                bin_ = briefio.convert_int(alp.index(char),6)

                # adding the key
                bin_ = briefio.String.map_string(bin_, add_key)
                bin_ = briefio.String.reverse(bin_)
                bin_chars.append(bin_)
                

            elif char in msc:bin_chars.append(msc[char])
            else: bin_chars.append(char)
        b.write(briefio.String.remove_last(briefio.String.fromArray(bin_chars, "-")) + "\n")
    
    f.close()
    b.close()

def reverse_bin_scramble(path, key=[0,0,0,0,0,0]):

    f = open(path, "r")
    b = open("reversed.txt", "w")

    def remove_key(char, index):
        return str( int(char) - key[index])
    
    for line in f:
        bins = briefio.String.list_separator(line, "-")
        dec_line = []
        for bi in bins:
            if bi in msc_: dec_line.append(msc_[bi])
            else:
                bi_ = briefio.String.reverse(bi)
                bi_ = briefio.String.map_string(bi_, remove_key)
                bi_ = briefio.convert_binary_int(bi_)
                if bi != "":dec_line.append(alp[bi_])
        
        b.write(briefio.String.fromArray(dec_line) + "\n")
    
    b.close()
    f.close()
                
convert_bin_scramble("dictionary.txt", [1,2,3,8,4,7])
reverse_bin_scramble("converted.bin", [1,2,3,8,4,7])
