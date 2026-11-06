from datetime import date

from university.models import Semester, Professor, Course, CourseDescription, Student, StudentID

semester1 = Semester.objects.create(start=date(2027, 1, 1), end=date(2027, 6, 30), course=["course1", "course2", "course3"])

professor1 = Professor.objects.create(first_name="John", last_name="Doe", email_address="john.doe@example.com", course="course1") 
professor2 = Professor.objects.create(first_name="Jane", last_name="Smith", email_address="jane.smith@example.com", course="course1") 
professor3 = Professor.objects.create(first_name="Alice", last_name="Johnson", email_address="alice.johnson@example.com", course="course3") 

course1 = Course.objects.create(name="Course A", number_of_modules=5.0) 
course2 = Course.objects.create(name="Course B", number_of_modules=3.0) 
course3 = Course.objects.create(name="Course C", number_of_modules=10.0) 

description1 = CourseDescription.objects.create(description="bla", course=course1)
description2 = CourseDescription.objects.create(description="blabla", course=course2)
description3 = CourseDescription.objects.create(description="blablabla", course=course3)

student1 = Student.objects.create(first_name="Johny", last_name="Doey")
student2 = Student.objects.create(first_name="Janey", last_name="Smithy")
student3 = Student.objects.create(first_name="Alicey", last_name="Johnsony")

student_id1 = StudentID.objects.create(student=student1)
student_id2 = StudentID.objects.create(student=student2)
student_id3 = StudentID.objects.create(student=student3)

