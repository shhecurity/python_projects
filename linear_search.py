array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    #search array
    i=0
    while i<len(array_to_search_through):
        if array_to_search_through[i]==value_to_find:
    #if value found,return index         
            return i
        i+=1
    #if not, return none
    return None   

def global_linear_search(value_to_find, array_to_search_through):
    found_index_list=[]
    i=0
    while i<len(array_to_search_through):
        if array_to_search_through[i]==value_to_find:
    #if value found,store the index in list    
            found_index_list.append(i)
        i+=1
    return found_index_list
    #if not, return none

# def linear_search_helper(value_to_find,array_to_search_through, find_one_or_all):
#     found_index_list=[]
#     i=0
#     while i<len(array_to_search_through):
#         if array_to_search_through[i]==value_to_find:
#             #if value found, store index
#             found_index_list.append(i)
#             #if only one found, retrun after first search
#             if find_one_or_all:
#                 return found_index_list
#             i+=1
#     return found_index_list