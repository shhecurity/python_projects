#Recursion
#       the process in which a function calls itself

#using recursion to solve a problem requires 2 cases:
#--     -a base case- the conditioon in which the function stops calling itself
        # -b- the recursive case - the case in which the function returns to itself
# example:


#itretative countdown
#for index in range (start, end, iteration amount)


import random
import pprint

def countdown_iterative():
    for i in range (20, 0, -1):
        print(i)

print(countdown_iterative())

print('iterative countdown complete')
# recursive countdown
# must have if and else statements so it has a start and an end
def countdown_recursive(num):
    print(num)
    #base case print the num, then check if the next num = 0, if it is, stop if not subtract one, and repeat.
    if num == 0:
        return
    else:
        countdown_recursive(num-1)#recursive case

print('countdown_recursive initiating. . . ')
countdown_recursive(15)

def countdown_from_21_recursive(num=21):
    print(num)
    if num == 0:#basecase
        return
    else:
        countdown_from_21_recursive(num-1)


print('first countdown from 21, recursive initiating:')
countdown_from_21_recursive()

print("modiified countdown from 21 to 12 initiating. . .")
countdown_from_21_recursive(12)

def countup_recursive(num=22, start=0): 
    print(start)
    if start == num:
        return
    else:
        countup_recursive(num,start+1)
      
def countup_recursive_2(num, count=1):
    print(count)
    if num == count:
        return
    else:
        countup_recursive_2(num, count+1)  

print('countup recursive')

countup_recursive()

print("count up recursive #2:")

countup_recursive_2(33)

# divide candy # - - recursive problem solving - - 
    # 1. start with current pile
    # 2. divide pile in half
    #     - if remainder, eat candy 
    # 3. other half of pile is current pile 
    # 4. divide pile in half (floor div)
    #     -if remainder eat candy
    # 5. stop at 0 candy
    
def divide_candy(candy, piles=[]):
    if candy == 0:
        return piles
    else:
        candy = candy//2
        piles.append(candy)
        return divide_candy(candy, piles)

print("divided candy:", divide_candy(50))
     
    
def sum_up_to(num):
    #base case
    if num ==1:
        return 1
    else:
        return num + sum_up_to(num-1)

print("sum up to 41",sum_up_to(41))

#|--------Iterative Example using while loop-----------------|#
def space_x_countdown(num):
    while num > 0:
        print(num)
        num = num-1
    return "Lift Off"

#|------------Recursive Example-------------------------|#
def space_x_recursive_countdown(num):
    if num == 0:
        return print("Lift Off")
    else:
        print(num)
        space_x_recursive_countdown(num-1)
        
print(space_x_countdown(5))
space_x_recursive_countdown(6)


#--|--|--|--Stack Methods In A Stack Class--|--|--|--|--|--#

# -a stack is a type of data struction
#    - The Call Stack stores executions of code on the stack in the order they are executed and 
#       removes them from the stack when they are done executing
#           -last in, first out



class Stack:
    def __init__(self):
        self._data_store=[]
    
    def push(self, fn):    
        self._data_store.append(fn)
        
    def pop(self):
        return self._data_store.pop()
  
    def get_store(self):
        return self._data_store
s = Stack()
s.push('hi')
s.push('there')
s.push('bye')  

print('stack class:', s._data_store)  
print(s.pop())
print(s._data_store)
  
  
 #create a function that returns a random integer variable and a string denoting the order
def create_stack(order):
    local = random.randint(1,100)
    frame = {
        "local_var": local,
        "func": f"this is a function called {order}"
    }
    return frame
      

    
s.push(create_stack("first"))
s.push(create_stack("second"))
s.push(create_stack("third"))

pprint.pprint(s.get_store())
pprint.pprint(s.pop())
pprint.pprint(s.get_store())


# def divide_Candy2(candy):
#     print(candy)
#     candy = candy//2
#     if candy == 0:
#         return
#     else:
#         divide_Candy2(candy)

# divide_Candy2(20)
