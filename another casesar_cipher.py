def caesar_cipher(string, shift_amount):
    #declaration of variables
    new_string = str()
    ascii_letter_value = int()
    one_letter = str()
    new_ascii_value=int()
    #loop to assign new ascii value
    for index in range(0, len(string)):
        one_letter = string[index]
        ascii_letter_value = ord(one_letter)
        if index=='!' or index ==',' or index == '.':
            new_string = new_string + index  
        
        # check if the letter is Z or z
        if ascii_letter_value == 122:
            new_ascii_value == 97
        elif ascii_letter_value == 90:
            new_ascii_value = 65
        #assign a new value if not Z or z
        else:
            new_ascii_value = ascii_letter_value + shift_amount
        #creating the new string
        new_string = new_string+ chr(new_ascii_value)
    
    
    return new_string
 


print(caesar_cipher('Boy! What a string!',5))

#make a dict of letters
#enumerate letters
#-_-_-_-_works in uppercase-_-_-_-_-_-_-_-_-_#
#shift every letter by 5
#output shifted string
def encrypt_character(char, shift_amount):
    return chr(ord('A')+(ord(char)- ord('A')+shift_amount)%26)



def caesar_cipher(string, shift_amount):
    string=string.upper()
    ciphertext= ''
    for char in string:
        if char not in ' ,.':
            ciphertext+= encrypt_character(char, shift_amount)
    return ciphertext
   
   
   

print(caesar_cipher("dsakjfhds", 5))