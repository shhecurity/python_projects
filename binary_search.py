# Here's the basic premise of the algorithm:

# 1. Say you're searching for a value `number_to_find` in a search set of `sorted_values`
# 2. Find the middle value in `sorted_values` we'll call `middle_value`
# 3. If `number_to_find` is equal to `middle_value` then your target is found
# 4. If `number_to_find` is less than `middle_value`, split your `sorted_values` in half and repeat the algorithm on your new subset (the half of `sorted_values` before `middle_value`)
# 5. If `number_to_find` is greater than `middle_value`, repeat step but with the half of `sorted_values `values` after `middle_value`
# 6. Repeat until you find `number_to_find` or return `-1` if it doesn't exist

# import random
# import statistics
# ```python

import random
values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

#create a method BINARY_SEARCH that takes in a number to find, a sorted array, and a TRACKER INDEX=0.
#find the middle index and assign to variable MIDDLE_INDEX
#find the middle number of the SORTED_ARRAY
# if the MIDDLE_NUMBER = TARGET_NUMBER 
#   then add MIDDLE_INDEX + TRACKER INDEX
# if TARGET_NUMBER is greater than MIDDLE_NUMBER 
#   then return half the sorted array, the half containing the larger numbers and pass it back into BINARY_SEARCH(NUM_TO_FIND, (smaller array, tracker_index+middle_index TRACKER_INDEX + MIDDLE_INDEX))

# [*, *, *, *, *,  7, *, *, *, *] tracker_index = 0
# [*, *, *, *, *] [7, *, *, *, *] num_to_find > 7 tracker_index = 5
# [7, *]

# if not already sorted
# # sorted_values = value_range.sort() , replace the value_range with sorted_values

def binary_search(num_to_find, value_range, tracker_index=0):
    middle_index = len(value_range)//2
    middle_number = value_range[middle_index]
    if len(value_range) <= 1:
        return -1
    elif num_to_find == middle_number:
        return tracker_index + middle_index
    
    elif num_to_find > middle_number:
         return  binary_search(num_to_find, value_range[middle_index:], tracker_index + middle_index)
    elif num_to_find < middle_number:
        return  binary_search(num_to_find, value_range[:middle_index], tracker_index)

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # sorted_values = value_range.sort()
    # middle_value = statistics.median(sorted_values)
    # middle_index = sorted_values.index(middle_value)
    # if num_to_find == middle_value:
    #     return value_range.index(num_to_find)
    # elif num_to_find < middle_value:
    #     sorted_values = sorted_values[:middle_index]
    #     binary_search(num_to_find, sorted_values)
    # elif num_to_find > middle_value:
    #     sorted_values = sorted_values[middle_index:]
    #     binary_search(num_to_find, sorted_values)
    # else: return -1
    

print(binary_search(537, values))# this returns the index of 537 in values if it exists and -1 if it doesn't exist


test_array = [1,2,3,4,5]
        
print(binary_search(1, test_array)) #== 0)
print(binary_search(2, test_array))#== 1)
print(binary_search(3, test_array)) #== 2)
print(binary_search(4, test_array)) #== 3)
print(binary_search(5, test_array)) #== 4)