from collections import Counter
def char_count(str):
  #remove spaces from string so they are not counted
  removed_spaces=str.replace(" ","")
  #count the items in the string using Counter function.
  return (Counter(removed_spaces))
  #either remove the dictionary from the return or remove the parentheses and "counter" from the return
  
  

print(char_count('an apple a day'))