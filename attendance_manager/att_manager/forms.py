from django import forms
from.models import Attendance

class AttendanceForm(forms.ModelForm):
    employee_name = forms.CharField(label='Employee Name')
    employee_code = forms.CharField(label='Employee Code')
    in_time = forms.TimeField(label='In Time')
    out_time = forms.TimeField(label='Out Time')

    class Meta():
        model = Attendance
        fields = '__all__'