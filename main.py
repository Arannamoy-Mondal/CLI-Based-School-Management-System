from classroom import Classroom
from person import Person,Student,Teacher
from school import School
from subject import Subject

school=School('Abc','Dhaka')
eight=Classroom("Eight")
nine=Classroom("Nine")
ten=Classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

#add student

std1=Student('Std1',eight)
std2=Student('Std2',nine)
std3=Student('Std3',ten)
std4=Student('Std4',ten)
std5=Student('Std5',nine)

school.student_admission(std1)
school.student_admission(std2)
school.student_admission(std3)
school.student_admission(std4)
school.student_admission(std5)

#add teacher

t1=Teacher('Teacher1')
t2=Teacher('Teacher2')
t3=Teacher('Teacher3')
t4=Teacher('Teacher4')

#add subject

sub1=Subject('Mathematics',t1)
sub2=Subject('Physics',t2)
sub3=Subject('Chemistry',t3)
sub4=Subject('Botany',t4)   

eight.add_subjects(sub1)
eight.add_subjects(sub2)
nine.add_subjects(sub3)
nine.take_semester_final_exam()
eight.take_semester_final_exam()
print(school)