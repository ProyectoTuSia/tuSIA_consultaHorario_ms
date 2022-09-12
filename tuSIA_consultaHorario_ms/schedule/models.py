# from django.db import models
from djongo import models
from django import forms

# Create your models here.

#from django.db import models


class Course(models.Model):
    courseId = models.PositiveIntegerField()
    name = models.CharField(max_length=70, blank=False, default='')
    professor = models.CharField(max_length=70, blank=False, default='')
    credits = models.PositiveIntegerField()
    building =models.CharField(max_length=200, blank=False, default='')
    classroom = models.CharField(max_length=100, blank=False, default='')
    group = models.PositiveIntegerField(max_length=100, blank=False, default='')
    type = models.CharField(max_length=70, blank=False, default='')
    timetable = models.CharField(max_length=70, blank=False, default='')

    class Meta:
        abstract = True


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = (
            "courseId","name","professor","credits","building","classroom","group","type","timetable")


class Schedule(models.Model):
    userId = models.CharField(max_length=70, blank=False, default='')
    monday = models.ArrayField(model_container=Course,model_form_class=CourseForm)
    tuesday = models.ArrayField(model_container=Course,model_form_class=CourseForm)
    wednesday = models.ArrayField(model_container=Course,model_form_class=CourseForm)
    thursday= models.ArrayField(model_container=Course,model_form_class=CourseForm)
    friday = models.ArrayField(model_container=Course,model_form_class=CourseForm)
    saturday = models.ArrayField(model_container=Course,model_form_class=CourseForm)



# objects = models.DjongoManager()  
