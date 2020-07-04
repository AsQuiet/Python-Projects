from binary import convert_int, convert_binary_int

def printRam(r):
    for key in r.keys():
        print(key + " - " + str(r[key]))

def createRam16B():
    ram = {}
    for x in range(16):
        ram[convert_int(x,4)] = createByte()
    return ram

def createByte():
    return [0,0,0,0,0,0,0,0]

def createReg1B():
    return createByte()

class PrgmCntr():
    def __init__(self,mx=16):
        self.current_value = -1
        self.max_value = mx
    def get_next_binary(self):
        self.current_value = (self.current_value + 1) if self.current_value + 1 < self.max_value else 0
        return convert_int(self.current_value, 4)

def createProgramCounter1B():
    return PrgmCntr()

class CPU():
    def __init__(self, alu, regA, regB, ram, pc):
        self.alu = alu
        self.regA = regA
        self.regB = regB
        self.ram = ram
        self.pc = pc
    
    def exe(self):
        
        ite=0
        while ite<50:
            ite+=1
            # getting next mem address from pc
            next_adress = self.pc.get_next_binary()

            # getting the byte stored at that mem adres
            stored_instruction = self.ram[next_adress]
            instruction = stored_instruction[0:4]
            mem_addres_ = stored_instruction[4:]
            mem_addres = cnvtBitStr(mem_addres_)
            
            # decoding the instruction
            if instruction == [1,1,1,1]:
                break
            elif instruction == [0,0,0,1]:
                # load into regA
                self.regA = self.ram[mem_addres]
            elif instruction == [0,0,1,0]:
                # load into regB
                self.regB = self.ram[mem_addres]
            elif instruction == [0,0,1,1]:
                # let alu calculate everything in regA and regB and put it in given addre
                calculated = self.alu.calc2x1B(self.regA, self.regB)
                self.ram[mem_addres] = calculated.copy()
            elif instruction == [0,1,0,0]:
                # print out the value
                self.bin_output(self.ram[mem_addres])
            

    
    def bin_output(self, b):
        print("[OUT] " + str(b))


class ALU():
    def __init__(self):
        self.value = []
    
    def calc2x1B(self, regA, regB):
        current_carry = 0
        result = []
        for i in range(len(regA)):
            index = len(regA) - i - 1
            s, nxt_c = addBit(regA[index], regB[index], current_carry)
            # print("adding " + str(regA[index]) + " and " + str(regB[index]) + " and carry of " + str(current_carry))
            # print("results are " + str(s) + " and new carry of " + str(nxt_c))
            result.append(s)
            current_carry = nxt_c
        result.reverse()
        return result

class Gates:
    @staticmethod
    def xor(a, b):
        return (a+b == 1)
    @staticmethod
    def and_(a,b):
        return a+b == 2

def addBit(b1, b2, c=0):
    s = Gates.xor(int(b1), int(b2))
    s = Gates.xor(s, int(c))
    c = Gates.and_(int(b1), int(b2)) or Gates.and_(int(b2), int(c)) or Gates.and_(int(b1), int(c))
    return 1 if s else 0, 1 if c else 0

def cnvtStrBit(s):
    bits = []
    for char in s:
        if char == " " :continue
        bits.append(int(char))
    return bits

def cnvtBitStr(b):
    s = ""
    for bit in b:
        s += str(bit)
    return s

def main():
    ram = createRam16B();

    ram["0000"] = cnvtStrBit("0001 1110")
    ram["0001"] = cnvtStrBit("0010 1111")
    ram["0010"] = cnvtStrBit("0011 1101")
    ram["0011"] = cnvtStrBit("0100 1101")
    ram["0100"] = cnvtStrBit("1111 0000")

    ram["1110"] = cnvtStrBit("00000011")
    ram["1111"] = cnvtStrBit("00001111")

    programCounter = createProgramCounter1B()
    regA = createReg1B()
    regB = createReg1B()
    alu = ALU()
    cpu = CPU(alu, regA, regB, ram, programCounter)   
    cpu.exe()
    printRam(cpu.ram)
    
if __name__ == "__main__":
    main();
    
