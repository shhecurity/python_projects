def recursive_roman_numerals(num):
    #create and object that stores roman numberal key and value
    roman_to_arabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I" : 1
        }
    answer = ""  
    if num > 0:
        answer = ""
        for roman in roman_to_arabic:
            arabic = roman_to_arabic[roman]
            if num >= arabic:
                counter=0
                times = num // arabic
                answer += roman * times
                num -= arabic * times
                return answer + recursive_roman_numerals(num)
    else:
        return answer
    
# print(recursive_roman_numerals(25))
# print(recursive_roman_numerals(598))
