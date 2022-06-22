# Destructive Methods/Functions => mutate or change the orginal list(array)/string/object/number
num_list = [1,4,8,9,12]
print(num_list)
num_list.append(20)
print(num_list)

num_list.insert(2, 22)#insert(index, NUM to insert)
print(num_list)

num_list.pop()
print(num_list)
num_list.insert(3, 5)
num_list.insert(4, 5)
print(num_list)
num_list.remove(5)
print(num_list)
num_list.sort()
print(num_list)

#NonDestructive Methods--> do not change the original, must be assigned to new variable to persist
num_list2 = [1, 4, 22, 5, 5, 8, 9, 12]

snum_list2 = sorted(num_list2)

print(snum_list2)

rnum_list2 = reversed(num_list2)
print(rnum_list2)

first_name = 'tom'
Tom = first_name.capitalize()
TOM = first_name.upper()
tom = first_name.lower()