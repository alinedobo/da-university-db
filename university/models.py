from django.db import models
from datetime import date

# Create your models here.
class Semester(models.Model):
    start = models.DateField(default="", blank=False)
    end = models.DateField(default="", blank=False)
    course = models.ManyToManyField("Course")

    def __str__(self):
        return f"{self.course}"


class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=50, blank=True, default="")
    course = models.ManyToManyField("Course")

    def __str__(self):
        return f"{self.last_name} {self.course}"


class Course(models.Model):
    name = models.CharField(max_length=50)
    number_of_modules = models.IntegerField(blank=True, default=1)
    #professor = models.ManyToManyField(Professor)
    #semester = models.ManyToManyField(Semester)

    def __str__(self):
        return f"{self.name}"


class CourseDescription(models.Model):
    description = models.CharField(default="", max_length=1000)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course} {self.description}"


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.last_name} {self.last_name}"


class StudentID(models.Model):
    expiration_date = models.DateField(default=date(2999, 12, 31),blank=False)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}"

