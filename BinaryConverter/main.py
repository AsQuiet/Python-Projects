import binaryconverter as b
import random

succes = True
for x in range(1000):

    n = random.random()
    i = b.convert_decimal(n, 1000)
    a = b.convert_binary_decimal(i)

    print("converting number : " + str(n) + " to  : " + i)
    print("converting back : " + i + " results in : " + str(a) + "\n")

    succes = succes and n == a

print(succes)

print(b.convert_binary_int("101110"))