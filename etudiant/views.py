from django.urls import reverse, reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render
from .forms import (
    EtudiantCreateForm
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
     FormView

)
from account.forms import UserCreateForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Etudiant
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.contrib import messages
from account.models import User


def register(request):
    if request.method == 'POST':
        user_form = UserCreateForm(data=request.POST)
        profile_form = EtudiantCreateForm(
            data = request.POST,
            files = request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.student = True
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user # set the user created to the profile
            if 'mugshot' in request.FILES:
                profile.mugshot = request.FILES['mugshot']
            profile.save()
            return HttpResponseRedirect(reverse('students_profile:student_profile_list'))
    else:
        user_form = UserCreateForm()
        profile_form = EtudiantCreateForm()
    return render(request,'students/profile/create_form.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })


class StudentListProfileView(ListView):
    model = Etudiant
    context_object_name = 'eleves'
    template_name = 'eleves/students_list/list.html'
    ordering = ['-student_class']



class StudentDetailProfileView(DetailView):
    model = Etudiant
    context_object_name = 'student_details'
    template_name = 'eleves/profile/dashboard.html'


class StudentUpdateProfileView(UpdateView):
    model = Etudiant
    template_name = 'eleves/profile/profile_form.html'
    form_class = EtudiantCreateForm
    
    # def get_success_url(self):
    #     return HttpResponseRedirect(reverse('students_profile:student_profile_detail', args=[self.object.id]))




class StudentDeleteProfileView(DeleteView):
    model = Etudiant
    success_url = reverse_lazy('students_profile:student_profile_list')
    template_name = 'eleves/profile/delete.html'




def upload_student(request):
    '''
    View for uploading Students
    '''
    # updoad student
    template_name = 'eleves/profile/upload.html'
    if request.method == 'POST':
        csvfile = request.FILES['etudiant']  # gets the input field name
        print(csvfile.name)  # prints the csv file name
        if not csvfile.name.endswith('.csv'):
            print("Invalid!!") # prints invalid at the console
            messages.errors(request, "CSV file format not supported")
            return(HttpResponseRedirect('etudiant:fail'))
        file_data = csvfile.read().decode("utf-8")  # reads the csv file
        # print(file_data)
        lines = file_data.split("\n") # split using the delimiter
        data_dict = {} # empty dictionary to store the csv data
        print(len(lines))
        for line in lines:
            print(line)
            fields = line.split(',')
            # print(fields)
            user_dict = {
                'email':fields[0],
                'password':fields[1],
                # 'password2':fields[2],
            }
            student_profile_dict = {
                'nom':fields[2],
                'prenom':fields[3],
                'niveau':fields[4],
                'genre':fields[5],
                'filiere':fields[6],
                'student_class':fields[7],
                'created_at':fields[9],
                'address':fields[10]
            }
            # print(len(data_dict))
            if data_dict != '':
                user = User.objects.create_user(
                    email=user_dict['email'],
                    password=user_dict['password']
                )
                user.student = True
                user.save()  # save the user
                student_profile = Etudiant.objects.create(
                    user = user,
                    nom = student_profile_dict['nom'],
                    prenom = student_profile_dict['prenom'],
                    niveau = student_profile_dict['niveau'],
                    filiere = student_profile_dict['filiere'],
                    genre=student_profile_dict['genre'],
                    student_class = student_profile_dict['student_class'],
                    created_at = student_profile_dict['date_admitted'],
                    address = student_profile_dict['address']
                )
                messages.success(request, "File Successfully Uploaded")
            else:
                messages.errors(request, "File not uploaded")
    context = {}
    return render(request, template_name, context)
