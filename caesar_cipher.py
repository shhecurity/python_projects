#create a method that takes in a string and a number to shift by
#create 2 variables of string of letters of the alphabet,UPPERcase and LOWERcase
#CURRENT_INDEX variable
#NEW_INDEX var
#CIPHER_TEXT var
    #VALIDATION var of a string of special characters
#For loop to loop through string
#If value at index i is in VALIDATION string
#append that value to the CIPHER_TEXT string
# else if current value exists in the UPPER var
#   CURRENT_INDEX equals index of the value in the UPPER var
    #if current values index + number parameter >= 0 and is < than the length of UPPER var
    #NEW_INDEX = current index + shift_amt 
    #ELIF current index + num param < 0
        #new_index = len(UPPER) + current_index + shift_amt
#    ELSE 
#       new_index = current_index +number - len(UPPER)
#   CIPHER_TEXT += UPPER(NEW_INDEX)
# else if current value exists in the LOWER var
#   CURRENT_INDEX equals index of the value in the LOWER var
    #if current values index + number parameter >= 0 and is < than the length of LOWER var
    #NEW_INDEX = current index + shift_amt 
    #ELIF current index + num param < 0
        #new_index = len(UPPER) + current_index + shift_amt
#    ELSE 
#       new_index = current_index +number - len(UPPER)
#   CIPHER_TEXT += LOWER(NEW_INDEX)


def caesar_cipher(string, shift_amount):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    current_index = 0
    new_index = 0
    cipher_text = ''
    special_chars = '1234567890!@#$%^&*(){}[]+=_-/`~|\?<>., '
    
    for i in range (len(string)):
        if string[i] in special_chars:
            cipher_text += string[i]

        if string[i] in upper:
            current_index = upper.index(string[i])
            
            if current_index + shift_amount >= 0 and current_index + shift_amount < len(upper)-1:
                new_index = current_index + shift_amount
            
            elif current_index + shift_amount < 0:
                new_index = len(upper)+ current_index + shift_amount
                
            else:
                new_index = current_index = shift_amount - len(upper)
            cipher_text += upper[new_index]
            
        if string[i] in lower:
            current_index = lower.index(string[i])
            
            if current_index + shift_amount >= 0 and current_index + shift_amount < len(lower)-1:
                new_index = current_index + shift_amount
            
            elif current_index + shift_amount < 0:
                new_index = len(lower)+ current_index + shift_amount
                
            else:
                new_index = current_index = shift_amount - len(lower)
            
            cipher_text += lower[new_index]

    print(cipher_text)
    return cipher_text
           
#caesar_cipher("Hello zach168! Yes here.", 5)