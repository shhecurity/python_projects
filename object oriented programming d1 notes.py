
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

# class is like the big IDEa 
# instances are the practical manifestations
  

