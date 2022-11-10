from django.urls import path
from . import views

app_name = 'etudiant'

urlpatterns = [
    path('',views.StudentListProfileView.as_view(), name='student_profile_list'),
    path('profile/create/', views.register, name='student_profile_create'),
    path('profile/upload/', views.upload_student, name='student_profile_upload'),
    path('<int:pk>/profile/', views.StudentDetailProfileView.as_view(), name='student_profile_detail'),
    path('<int:pk>/update/', views.StudentUpdateProfileView.as_view(), name='student_profile_edit'),
    path('<int:pk>/profile/delete/', views.StudentDeleteProfileView.as_view(), name='student_profile_delete')
]