import random
from school import School
class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evaluate_exam(self):
        return random.randrange(1,100)
    
class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.clasroom=classroom
        self.__id=None
        self.marks={}
        self.subject_grade={}
        self.grade={}

    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            sum+=School.grade_to_value(grade)
        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

    @property # getter method
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.id=id
