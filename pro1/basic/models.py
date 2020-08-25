from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    owner_name=models.CharField(max_length=20)
    type_c=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Problems(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    problem=models.CharField(max_length=20)
    from_date=models.DateField()
    to_date=models.DateField()
    image_c=models.ImageField(blank=True)

    def __str__(self):
        return self.problem

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE)
    branch=models.CharField(max_length=20)
    education=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Solution(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    solution=models.CharField(max_length=20)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField()
    address=models.CharField(max_length=30)

    def __str__(self):
        return self.solution

class Solution_Progress(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    to_date=models.DateField()
    solution=models.ForeignKey(Solution,on_delete=models.CASCADE)
    progress=models.CharField(max_length=20)
    progress_details=models.TextField()
    image_c=models.ImageField(blank=True)
