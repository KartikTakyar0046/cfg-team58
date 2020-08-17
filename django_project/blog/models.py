from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class Students(models.Model):
#     Name = models.CharField(max_length=100)
#     BatchId = models.TextField()
#     date = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.Name

class Passouts(models.Model):
    Region = models.IntegerField()
    LCDM_Name = models.CharField(max_length=100)
    LDC_Name = models.CharField(max_length=100)
    Batch_Code = models.CharField(max_length=100)
    Status = models.CharField(max_length=1)
    Start_Date = models.IntegerField()
    End_Date = models.IntegerField()
    Course_Name = models.CharField(max_length=100)
    Full_Name = models.CharField(max_length=100)
    DOB = models.IntegerField()

    def __str__(self):
        return self.Full_Name


class Batches(models.Model):
    Region = models.IntegerField()
    Center_Name = models.CharField(max_length=100)
    LDCM = models.CharField(max_length=100, default="")
    LDCM_Name = models.CharField(max_length=100)
    Reportee = models.CharField(max_length=100)
    Batch_Type = models.CharField(max_length=100)
    Batch_Code = models.CharField(max_length=100)
    Course_Name = models.CharField(max_length=100)
    Course_Name2 = models.CharField(max_length=100)
    Status = models.CharField(max_length=1)
    Start_Date = models.IntegerField()

    def __str__(self):
        return self.LDCM_Name


class Placement(models.Model):
    Region = models.IntegerField()
    ReporteeLDCM = models.CharField(max_length=100)
    LDC_Name = models.CharField(max_length=100)
    Batch_Code = models.CharField(max_length=100)
    Course_Name = models.CharField(max_length=100)
    Start_Date = models.IntegerField()
    End_Date = models.IntegerField()
    Student_Id = models.IntegerField()
    Student_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Student_Name
