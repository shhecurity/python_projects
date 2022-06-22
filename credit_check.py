def credit_check(str):
    if(len(str)!= 16):
          return "Invalid input!"
       #initialize list to append digits
    digits=[] #[1,2,3,4,.,.,.,]
        # convert digits to individual integers & add to list
    for char in str:
           num=int(char)
           digits.append(num)
           #double ever other number beginning with the first number
    for i in range (0,16,2):
                digits[i]*=2
                
        #check list for double digit number and add digits together, (for 10-19, the sum of the digits is equal to subtracting 9 from the digits, ie: 15:1+5=6, 15-9=6)
                if digits [i]>9:
                    digits[i]=digits[i]-9
        #sum all digits in the list
    sum=0
    for i in digits:
        sum+=1
        
        #output string message "num is valid" "or num is invalid"
    if sum % 10 == 0:
        return "The number is valid!"
    else: 
        return "The number is not valid!"               
   
   
# print(credit_check("6011797668867828"))
# print(credit_check("5541808923795240"))
# print(credit_check("5541808923795240"))                     
# print(credit_check("55418795240"))                     

# Your Luhn Algorithm Here
# Expected Output:
# If it is valid, print "The number is valid!"
# If it is invalid, print "The number is invalid!"

