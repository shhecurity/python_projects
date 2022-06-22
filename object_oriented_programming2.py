class Person:
    #class variables
    num_of_eyes = 2
    num_of_legs = 2
    num_of_fingers = 10
    
    
    def __init__(self, name, birthday, occupation, age, gender):
        self.name = name
        self.birthday = birthday
        self.occupation = occupation
        self.age = age
        self.gender = gender
        
    def say_hello(self):
        return f"Hello, my name is {self.name}.  My birthday is {self.birthday}.  My occupation is {self.occupation}.  I am {self.age} years old.  I am a {self.gender}."

    def increase_age(self):
        self.age += 1
        return f"My new age is {self.age}"  
    
    def change_jobs(self, new_job):
        self.occupation = new_job
        return f"My new job is {self.occupation}."
    
    def new_city(self, city):
        self.city = city
        return f"I just moved to {self.city}"
    
tom = Person('Tom', '12/12/88','lawyer', 33, 'male')
jon = Person('Jon', '4/6/79' ,'programmer', 38, 'male')

print(tom.say_hello())
print(jon.say_hello())

print(tom.increase_age())

print(tom.increase_age())

print(tom.increase_age())

print(tom.change_jobs('fireman'))

print(tom.say_hello())
print(tom.new_city('tampa'))
print(tom.city)
