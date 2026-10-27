from django.db import models


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)

    teachers = models.ManyToManyField(
        "Teacher",
        related_name="students",
        blank=True
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)

    def __str__(self):
        return self.name