from django.db import models

# Create your models here.

class StudentModel(models.Model):
    student_name=models.CharField(max_length=255)
    age=models.CharField(max_length=255)
    ten_th_marks=models.CharField(max_length=50)
    twelt_th_marks=models.CharField(max_length=50)
    class Meta:
        ordering=('id',)
        db_table = 'student_details'
    def __str__(self):
        return self (student_name)
                                    