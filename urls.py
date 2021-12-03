from django.urls import path
from ProManager import views
from .views import ExerciseDetailView
from .views import ProjectDetailView
from django.views.generic import ListView
from . import views

from . import views

urlpatterns = [
    path('exercise/<int:pk>/', ExerciseDetailView.as_view(), name='exercise-new'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-new'),
    path('register',views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name= "logout"),
    path('project', views.project, name="project"),
    path('', views.project, name="project"),
    path('exercise', views.exercise, name="exercise"),
    path('contact', views.contact, name="contact"),
    path('log', views.log, name="log"),
    path('create_project',views.create_project, name="create_project"),
    path('create_exercise',views.create_exercise, name="create_exercise"),
    path('project/<int:pk>/update', views.ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('exercise/<int:pk>/update', views.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('exercise/<int:pk>/delete', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
    path('exercise/<int:pk>', views.comment, name='exercise_comment'),   
]

