from django .conf.urls import url
from .import views

urlpatterns=[
    url('^$',views.IndexView.as_view(),name='index'),
    url('^Attendance/$',views.AttendanceView.as_view(), name='attendance_list'),
    url('^Create-Entry/$', views.CreateEntryView.as_view(), name='create_entry'),
    url('^Edit-Entry/(?P<pk>\d+)/$', views.AttendanceEditView.as_view(), name='attendance_edit'),
    url('^Delete-Entry/(?P<pk>\d+)/$', views.AttendanceDeleteView.as_view(), name='attendance_delete'),

]