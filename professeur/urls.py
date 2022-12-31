from django.urls import path
from . import views

app_name = 'professeur'

urlpatterns = [
    path('', views.TeacherListProfileView.as_view(), name='teacher_profile_list')
]