# How can you make this more scalable and reusable later?


#-------PseudoCode-----------#
#   1. create a list for Armstrong nums
#   2. iterate/loop through the range of numbers
#   3. convert numbers to strings
#   4. get string length,
#   5. create var EXPONENT and  have it == string length
#   6. create a variable called SUM and have its initial value as 0
#   7. create a TEMP var that stores a number to extract each individual integer from the number, initial value of NUM
#   8. create a while loop where TEMP is GREATER THAN 0
#   9. find remainder of TEMP using %(modulus)10 to get the last integer and store that into a variable called DIGIT
#   10.take DIGIT to power of EXPONENT var and + to sum
#   11. re asses TEMP var at the floor of the TEMP divided by 10.
#   12.  write and IF STATEMENT that checks if NUM is = to SUM and if true, add to LIST
def find_armstrong_numbers(numbers):
    #create a list for Armstrong nums
    armstrong= []
    #iterate/loop through the range of numbers, get string length,
#   5. create var EXPONENT and  have it == string length
    for num in numbers:
    # convert numbers to strings, create var EXPONENT and  have it == string length   
        exponent=len(str(num))
    #create a variable called SUM and have its initial value as 0    
        sum=0
    #create a TEMP var that stores a number to extract each individual integer from the number, initial value of NUM    
        temp=num
    #create a while loop where TEMP is GREATER THAN 0    
        while temp>0:
    #find remainder of TEMP using %(modulus)10 to get the last integer and store that into a variable called DIGIT
            digit= temp%10
    #take DIGIT to power of EXPONENT var and + to sum
            sum+=digit**exponent
    #re-assess TEMP var at the floor of the TEMP divided by 10.
            temp//=10
    #write and IF STATEMENT that checks if NUM is = to SUM and if true, add to LIST
        if num == sum:
            armstrong.append(num)
    return armstrong

#print(find_armstrong_numbers(list(range(0, 999))))
            
            
        