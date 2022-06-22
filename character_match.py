# Don't forget to run your tests!
from collections import Counter
def is_character_match(string1, string2):
	 # implementing counter function
    string1=string1.replace(" ","")
    string2=string2.replace(" ","")
    if(Counter(string1.lower()) == Counter(string2.lower())):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 		#string1.lower().count(string2.lower())
	