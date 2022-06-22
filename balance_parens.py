#------Pseudo------#
#1. input a string with letters, nums, or parens
#2. balance string by checking characters for parens and balancing parens
#3. return value should be balanced string

def balance_parens(str):
    balanced_str=""
    #if we get an opening parens(, then we may have a closing), so create a list to store until match found
    open_parens_index_list = []
    #loop through entire string
    for i, char in enumerate(str):
    #if we get a letter or number(non-parens) add the character to str
        if char !="(" and char != ")":
            balanced_str += char
    #if we get an openin g parens(, then we may have a closing)        
        elif char == "(":
            #append list of open parens(
            balanced_str+=char
            open_parens_index_list.append(len(balanced_str)-1)
            # print(i,open_parens_index_list)
#if we get a closing ), check for matching opening paren buddy(
        else:
            if len(open_parens_index_list) == 0:
                continue
            else:
                open_parens_index_list.pop()
                # print(i,open_parens_index_list)
                balanced_str += char
    # print("leftover open parens(")
    # print(i, open_parens_index_list)
    
    fully_balanced_str=""
    for i, char, in enumerate(balanced_str):
        if i not in open_parens_index_list:
            fully_balanced_str += char
    
    #return value should be a str (balanced)
    return fully_balanced_str

# output = balance_parens("a(b)(c)())") #should return "a(b)(c)()"
# output1= balance_parens("((((((((") #should return ""
# output2= balance_parens("((a(b)cd")
# print(output)
# print(output1)
# print(output2)