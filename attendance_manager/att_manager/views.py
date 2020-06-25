from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,ListView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import AttendanceForm
from .models import Attendance
# Create your views here.
class IndexView(TemplateView):
    template_name = 'att_manager/index.html'


class CreateEntryView(CreateView):
    form_class = AttendanceForm
    template_name = 'att_manager/create_form.html'


class AttendanceView(CreateView,ListView):
    template_name = 'att_manager/attendance_list.html'
    model = Attendance
    context_object_name = 'attendance'
    form_class = AttendanceForm


    def get_queryset(self):
        attendance = Attendance.objects.all()
        query = self.request.GET.get('name')
        print(query)
        if query:
            attendance = attendance.filter(Q(employee_name__icontains=query) | Q(employee_code__icontains=query))
        return attendance









        # try:
        #     name = self.kwargs['q']
        # except:
        #     name = ''
        # if (name != ''):
        #     object_list = self.model.objects.filter( Q(employee_name__icontains = name)| Q(employee_code__icontains = name))
        # else:
        #     object_list = self.model.objects.all()
        # return object_list
        # print(obje)

class AttendanceEditView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'att_manager/att_update.html'
    context_object_name = 'user'

class AttendanceDeleteView(DeleteView):
    model = Attendance
    context_object_name = 'user'
    template_name = 'att_manager/att_confirm_delete.html'
    success_url = reverse_lazy('attendance_list')


