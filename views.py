import re
from django.contrib.messages.api import error, success
from django.views.generic import DetailView,UpdateView,DeleteView,View
from django.utils.timezone import datetime
from django.shortcuts import render ,redirect ,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse







def project(request):
    projects = Project.objects.order_by('name')
    return render(request, "ProManager/project.html", {'projects':projects})

def exercise(request):
    exercises = Exercise.objects.all()
    return render(request, "ProManager/exercise.html", {'exercises':exercises})

def contact(request):
    return render(request, "ProManager/contact.html")
    
def log(request):
    return render(request, "ProManager/log.html")

def ProManager_there(request):
    return render(
        request,
        'ProManager/ProManager_there.html',
        {
            'date': datetime.now()
        }
    )



class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'ProManager/exercise_new.html'
    context_object_name = 'exercises'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'ProManager/project_new.html'
    context_object_name = 'projects'

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'ProManager/create_project.html'
    form_class = ProjectForm

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = "/project"
    template_name = 'ProManager/delete_project.html'

class ExerciseUpdateView(UpdateView):
    model = Exercise
    template_name = 'ProManager/create_exercise.html'
    form_class = ExerciseForm

class ExerciseDeleteView(DeleteView):
    model = Exercise
    success_url = "/project"
    template_name = 'ProManager/delete_exercise.html'

def register_request(request):
    if request.method == "POST":
	    form = NewUserForm(request.POST)
	    if form.is_valid():
		    user = form.save()
		    login(request, user)
		    messages.success(request, "Registration successful." )
		    return redirect("project")
	    messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="ProManager/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("project")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="ProManager/login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("project")


def create_project(request):
    error = ''
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('project')
        else:
            error = 'Form is not correct'

    form = ProjectForm()
    data = {
        'form': form,
        'error': error

    }
    return render(request,"ProManager/create_project.html", data )


def create_exercise(request):
    error = ''
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('exercise')
        else:
            error = 'Form is not correct'

    form = ExerciseForm()
    data = {
        'form': form,
        'error': error
        }
    return render(request,"ProManager/create_exercise.html",data)


def comment(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(Exercise, pk=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(exercise, pk)
    else:
        form = CommentForm()
    return render(request, "ProManager/exercise_new.html",
                  {"new": new,
                   "comments": comment,
                   "form": form})
