from django import forms
from django.contrib.contenttypes import fields
from django.db.models.fields import TextField
from django.forms import ModelForm,TextInput, Textarea ,DateTimeInput,Select,DateInput,ClearableFileInput,TimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import Select
from .models import *



# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
	    model = User
	    fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
	    user = super(NewUserForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']
	    if commit:
		    user.save()
	    return user

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ('name', 'description', 'full_descrip')

		widgets = {
			"name": TextInput(attrs={
				'class':'form-control',
				'placeholder':'Name Project'
			}),
			"description": TextInput(attrs={
				'class':'form-control',
				'placeholder':'Description'
			}),
			"full_descrip": Textarea(attrs={
				'class':'form-control',
				'placeholder':'Full description',
				'id':'exampleFormControlTextarea1',
				
			})
		}

class ExerciseForm(ModelForm):
	class Meta:
		model = Exercise
		fields = ('topic', 'description','end_date','time','type_of_exercise','task_of_priority','author','post')
		
		widgets = {
			"topic": TextInput(attrs={
				'class':'form-control',
				'placeholder':'Name Project',
				'aria-describedby':'basic-addon1'
			}),
			"description": Textarea(attrs={
				'class':'form-control',
				'placeholder':'Description',
				'aria-label': 'Description',
			}),
			"end_date": DateInput(attrs={
				'class':'form-control',
				'placeholder':'End data',
				'id':'date',
				'type':'date'
			
			}),
			"time": TimeInput(attrs={
				'class':'form-control',
				'placeholder':'Time',
				'id':'time',
				'type':'time'
			
			}),
			"type_of_exercise": Select(attrs={
				'class':'form-select',
				'placeholder':'Type exercise',
				'id':'inputGroupSelect01'
			}),
			"task_of_priority": Select(attrs={
				'class':'form-select',
				'placeholder':'Task priority',
				'id':'inputGroupSelect01'
			}),
			"author": Select(attrs={
				'class':'form-control',
				'placeholder':'Author ',
			
			}),
			"post": Select(attrs={
				'class':'form-control',
				'placeholder':'Author ',
			
			}),
		}

class CommentForm(ModelForm):
    """Форма комментариев к статьям
    """
    class Meta:
        model = Comments
        fields = ('text','user' )