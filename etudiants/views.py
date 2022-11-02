from django.shortcuts import render, redirect

# Create your views here.
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect("/home")
    else:
        form = StudentForm()

    return render(request, 'main/create_post.html', {"form": form})