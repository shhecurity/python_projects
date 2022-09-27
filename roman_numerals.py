# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
roman_numerals=[
    {"arabic":1000, "roman":"M"},
    {"arabic":900, "roman":"CM"},
    {"arabic":500, "roman":"D"},
    {"arabic":400, "roman":"CD"},
    {"arabic":100, "roman":"C"},
    {"arabic":90, "roman":"XC"},
    {"arabic":50, "roman":"L"},
    {"arabic":40, "roman":"XL"},
    {"arabic":10, "roman":"X"},
    {"arabic":9, "roman":"IX"},
    {"arabic":5, "roman":"V"},
    {"arabic":4, "roman":"IV"},
    {"arabic":1, "roman":"I"},
]
num = int(input("Please enter a number to covert to Roman Numeral: "))
def to_roman(num):
    rom_num=""#empty string to return    
    for conv_data in roman_numerals:
    
        #how many time does each arabic number go into the number supplied to the function
        copies=num//conv_data["arabic"]
        for i in range(copies):
            rom_num+= conv_data["roman"]
    #determine the remainder:
        num= num% conv_data["arabic"]
    return rom_num
    print(rom_num)
 
#print(to_roman())
