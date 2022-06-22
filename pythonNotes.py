
# Python
# two types of types:

# primative types- numbers, strings, booleans

# non-primative types - lists, dictonaries, functions, etc.

# python- assign variables with =
# there is no var, const, or let
# python uses snake_case while js uses camelCase
#python is 'whitespace sensitive' meaning that boundaries of programs(blocks, functions, etc.) are not limited by semicolons ; and braces[],{}, instead by 
# newlines and 
#   indentations

#primative types-

from copy import copy


a_small_number = 4 # a literal number

# arithmatic and logical operators
# +,-,*,/,//,%.<,>,==,!=
# no type cooersion, python can only compare the same types

a_string = 'hello world'
string_two="welcome to python"
print(type(a_string))

# string interpolation, 'f-string'
day='friday'
activity='bowling'
#example
(print(f"let's go {activity} on {day} afternoon"))

# booleans
boolean_true=True
boolean_false=False
#list, like arrays in js
berries=['grape','tomato','cucumber','eggplant','banana', 'watermelon','pumpkin']

#python supports negative list indices
print(berries[-1])
#prints pumpkin, neg index does not start at 0, but -1
#equivilent jscode:
# console.log(berries[berries.length-1])

#slice lists
print(berries[2:4])
#returns ['cucumber', 'eggplant'], does not return last value[4]

#python has a structure called 'tuples' that are like lists, but they are immutable, meaning they can not be mutated.  use ()instead of[]

days_of_the_week = ('monday','tuesday','wednesday','thursday' 'friday', 'saturday', 'sunday')
weekend = days_of_the_week[4:]
print(weekend)
print(days_of_the_week[0],days_of_the_week[5])
location=(25.5, 125.6)

#dictionaries
guy={
    'name':'Guy',
    'age': 44,
    'job': 'programmer'
    }
#must use bracket notation to access dictionaries in python
#dot notation only works for object
print(guy['age'])

people =[
    {
        'name':'alice',
        'age': 22,
        'job': 'coach'
    },
    {
        'name':'jim',
        'age':66,
        'job':'farmer'
    },
    {
        'name':'carol',
        'age': 55,
        'job': 'entrepenuer'
    }
    
] 
print(people[1]['name'])

def gimme_five(): 
    return 5
print(gimme_five())

def add_one(n):
    return(n+1)
print(add_one(20))
    
def describe_berries(n, color):
    print(f'I have {n} {color} berries.')
    
describe_berries(4, 'blue')

# use a * infront of a variable to give it any number of postional arguments (args)
def print_them_all(*args):
    print(args)

print_them_all('alice', 'jim', 'carol')

# a parameter with ** two asterics, can handly any number of keyword arguments
def who_am_i(**kwargs):
    for kwarg in kwargs:
        print(f'my {kwarg} is {kwargs[kwarg]}.')

who_am_i(name='dan', age=40,job='singer')
    
def kwargss(**keyword_dictionary):
    for this_one_keyword in keyword_dictionary:
        print(f'My {this_one_keyword} is {keyword_dictionary[this_one_keyword]}.')
kwargss(name='ben', age=30, job='teacher')

# Logic
# while JS uses &&, ||, !,  python uses words: and or not

def can_drink_beer(age, country):
    if age >=21 or age >=18 and country =='Canada':
      return True
    elif country=='Antartica': 
      return True
    else: return False
    
print (can_drink_beer(21, 'USA'))
print (can_drink_beer(20, 'USA'))
print (can_drink_beer(18, 'Canada'))
print (can_drink_beer(12, 'Antartica'))

#loops

my_list=['a', 'b', 'c', 'd']
for x in my_list:
    print(x)
    
#built in function range(), creates a list from 0 to the number you specify
for x in range(10):
    print(x)

for i, x in enumerate(my_list):
    print(i, x)
#prints 0 a, 1 b, 2 c, 3 d

my_set=set()
my_set={5,7,5,4,7,9}#returns {9,4,5,7}
print('my set:',my_set) # returns {'p', 'i','s','M'}
my_set=set('Mississippi')
print('my next set:',my_set)

food_reviews={
    'donuts':"yummy",
    'green beans':'ok',
}
for key in food_reviews:
    print (key)
    print (food_reviews[key])
    print ('=-=-=-=')

# while loop-  
#there should be something in the body of the while loop that can make the condition false
#countdown while loop:
x=9
while x>=0:
    print(x)
    x=x-1 

#String Methods

first_name= 'jonathan'
new_first_name = first_name.capitalize()
print(new_first_name)

last_name = 'young'
new_last_name = last_name.replace('g', '123')
print(new_last_name)

#string methods- are non-destructive on strings
#list methods- 
staff= ['jon', 'jack', 'john', 'jan']
staff.append('alicia')
print (staff)
staff.pop()
staff.pop()
print(staff)
#other useful methods
#string - find
#string - split
#string- join

#list/array- 
#list- append
#list - pop
#list- sort
# list- copy
# list- reverse

#javascript is the only language for the front end
#python is a good choice to run the back end - may devs building back

#traditional syntax
def my_regular_function(x,y):
    print(x,y)

#lamda functions
my_anon_function = lambda x,y:print(x,y)

my_new_list = [2,4,6,8]
#map

new_new_list = list(map(lambda item: item * -1, my_new_list))
print(my_new_list)
print(new_new_list)
#filter
filtered_list=filter(lambda item:item<5,my_new_list)
print(list(filtered_list))

#reduce
import functools

value= functools.reduce(lambda agg, item: agg + item, my_new_list)
print(value)

#ternary
time=11
x='cereal' if time<12 else 'sandwich'

food=time<12 and "breakfast"
print(food)

#list comprehensions (single line for loops)

#standard loop
my_new_list = []
for i in range (3,30,5):#(starting, ending, and iteration amount)
     my_new_list.append (i)
print(my_new_list)
#lc loop
my_latest_list=[i for i in range(3,30,5)]
print(my_latest_list)
#for in -loop in  objects
#for of -loop through array


# goals of a software developer

# 1. solve a problem
# 2. solve a problem well:
#     structurally
#     functionally
#     algorithmically
    
# improving your code
    
#     structurally-
#     code organization
#     system architecture
#     future-proofing(best you can)
#     reliability
#     readability
    
# programming paradigms

# ex:
#     -object oriented Programming
#     -functional Programming
#     procedural Programming
#     structured programming
#     logical Programming
    
# fundamental features of OOP (object oriented programming)
#     inheritance - sharing of similar features
#     polymorphism - objects can take different forms depending on needs & situations
#     abstraction - Logic/Complexity is hidden, for simplicity
#     Data Encapsulation - Data access can be restricted based on needs

# Classes 
# -User defined data types 
# -Used to tightly bind data and data manipulation methods together
# -Useful for mapping real world Things 
# - Represents a concept(or bluprint) for data from which objects (or "instances") are created 

# two main times found in a class:
#     - attributes = data members, ie variables 
#     - methods = functions that interact upon your data Members




#dog Example

owner = "zach"
name = "baxter"
breed = "lab"
color= "black"

def print_dog_details(owner, name, color, breed):
    print(f"{owner}'s dog is named {name}, and is a {color} {breed}.")



class Dog:
    species = "Canis Lupus Familiaris" # example of a *class attribute*
    sound = "Woof"
    legs = 4

    def __init__(self, name, breed):
        self.name = name # example of an *instance attribute*
        self.breed = breed

    def __str__(self):
        return f"I am a dog named {self.name} and my breed is {self.breed}. I have {self.legs} legs and I say {self.sound}!"

    def speak(self): # example of an *instance method*
        print(self.sound)

fido = Dog("fido", "Pointer") # create an instance of Dog, with some attributes
fido.speak()
print(fido) # much more descriptive output! This comes from the __str__() instance method

# Instance Attributes -vs- Class Attributes

# Instance attributes are variables that are unique to each instance of a class that is created
# Class attributes are variables that are shared between ALL instances of a class that are created
class Dog:
    species = "Canis Lupus Familiaris" # all dogs have the same species type => class attribute
    legs = 4
    sound = "woof"
    counter = 0
    # init makes it easier to create new instances of a class and makes sure they all have certain attributes, they if there are 4 parameters in your function, you must have 4 in your function call.  they can set default values and then you can call without all params.
    def __init__(self, name, breed, color, legs = 4):
        self.name = name # each dog has a unique name => instance attribute
        self.breed = breed
        self.color = color
        
        Dog.counter += 1
    
    def speak(self): #example of an *instance method*
        print(self.sound)
        
    def update_sound(self, new_sound):#changing a class attribute with an instance level attribute, self will also give preferance to instance level attributes vs class level attributes.
        self.sound= new_sound
    def __str__(self):#when print(instance), will print given return string
        return f"I am a dog named {self.name} and my breed is {self.breed}. I have {self.legs} legs and I say {self.sound}!"    
    def __add__ (self, otherDog):#add two instances together under the same class
        breed = self.breed+otherDog.breed
        color = self.color+otherDog.color
        puppy = Dog("",breed,color)
        return puppy
    
hero = Dog("Hero", "Poodle", "blue")
hero.legs=3

baxter=Dog("Baxter", "lab", "black and white")       
fido = Dog("fido", "sharpei", "grey")
lassie = Dog("lassie", "pitbull", "brindle")
nova = Dog("Nova", "lab", "black with white spot")

print(fido.name)
print(fido.species)

print(lassie.name)
print(lassie.species)

print(nova.name, nova.species, nova.legs, nova.color)
nova.speak()
lassie.update_sound("bark!!")
lassie.speak()
print(hero.legs, "is the number of legs on hero")
print(nova)
print(hero)
new_puppy = nova + hero
print(new_puppy)
#Class level attributes VS Instance level Attributes
# - Class Attributes are values universal to all instances
#     eg: species name, chromosome cont, etc,
    
# - Instance Attributes are values that are unique to indivual instances
#     eg: name, age, etc.

# Dunder Methods of Python Classes
#   special built in class methods
#   examples:
#   - __init__()
#   - __str__()
#   - __repr__() 
#   - __eq__()
#   - __add__()
#   - __dict__()
# and many more