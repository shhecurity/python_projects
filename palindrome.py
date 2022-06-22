def palindrome(word):
    # check if input is an integer, if yes, convert to string
    if type(word) == int:
       word= str(word)   
    #reverse all the words
    reverseword = word[::-1]
    #check if palindrome
    if reverseword==word:
        return True 
    #if not yet, lower case, remove spaces, remove periods, remove comma, remove dash, check again if palindrome then return True for palindrome or false for not.
    else:
        lowerword = word.lower()
        nospace = lowerword.replace(" ","")
        noperiod=nospace.replace(".","")
        nocomma=noperiod.replace(",","")
        nodash=nocomma.replace("-","")
        reverseword = nodash[::-1]
        if reverseword == nodash:
            return True
        else: return False 
    


# print(palindrome('racecar'))
# print(palindrome ("hannukah"))
# print(palindrome('Sore was I ere I saw Eros.'))
# print(palindrome('A man, a plan, a canal -- Panama'))