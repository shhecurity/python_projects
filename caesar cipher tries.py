#make a dict of letters
#enumerate letters

#shift every letter by 5
#output shifted string
def caesar_cipher(string, shift_amount):
    #create a list to store ascii values
    
    
    for i in range (len(string)):
        if ord(string[i])<=ord("Z") and ord(string[i])>=ord("A"):
            ascii_code= ord(string[i])+shift_amount
            while ascii_code>ord("Z"):
                ascii_code = ascii_code - ord("Z")+ord("A")-1
            string[i]=chr(ascii_code)
        
        elif ord(string[i]) <= ord("z") and ord(string[i])>= ord("a"):
            ascii_code= ord(string[i])+shift_amount
            while ascii_code > ord("z"):
                ascii_code = ascii_code - ord("z")+ord("a")-1
            string[i] = chr(ascii_code)
            return "".join(string)
        
print(caesar_cipher("dsakjfhds", 5))