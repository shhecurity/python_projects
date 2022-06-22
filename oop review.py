

class Student:
    num_of_students_enrolled = 0
    
    
    
    def __init__(self, first_name, last_name, id, major, enrolled=False):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.major = major
        self.enrolled = enrolled
        
        
    def enroll_student(self):
        self.enrolled = True
        Student.num_of_students_enrolled +=1
        return self.enrolled
        
    def __str__(self):
        return f"Student name {self.first_name} {self.last_name}.  Student id: {self.id}.  Major: {self.major}. Enrollment Status:{self.enrolled}"   
        
        
tom = Student('tom', 'timey', 1234, 'cs')
joan = Student('joan', 'jalla', 4321, 'photography')
tom.enroll_student()
print(Student.num_of_students_enrolled)
joan.enroll_student()
print(Student.num_of_students_enrolled)




print(tom)
print(joan)