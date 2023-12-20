from StudentApp.models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['id','student_name','age','ten_th_marks','twelt_th_marks']
        