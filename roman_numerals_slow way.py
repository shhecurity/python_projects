# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
def to_roman(num):
    rom_num=""    
    
    increment=10
    rom_10="X"
    copies=num//increment
    for i in range(copies):
        rom_num+=rom_10
    num= num% increment
    increment=5
    rom_5="V"
    copies=num//increment
    for i in range(copies):
        rom_num+=rom_5
    num=num%increment
    increment=1
    rom_1="I"
    copies= num//increment
    print("copies", copies)
    for i in range(copies):
        rom_num+=rom_1
    print("final:", rom_num)
 
 
print(to_roman(27))