from django.db import models
# Create your models here.
from django.urls import reverse

class Attendance(models.Model):
    employee_name = models.CharField(max_length=20)
    employee_code = models.CharField(max_length=30)
    in_time = models.TimeField()
    out_time = models.TimeField()
    hours_worked = models.IntegerField()
    over_time = models.IntegerField()


    def __str__(self):
        return self.employee_name

    def get_absolute_url(self):
        return reverse('attendance_list')

