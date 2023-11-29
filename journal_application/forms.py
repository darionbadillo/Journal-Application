from django.forms import ModelForm
from .models import *
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

#create class for project form
class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields =('title', 'description', 'content')
        
#create class for notebook form
class NotebookForm(ModelForm):
    class Meta:
        model = Notebook
        fields =('title', 'about', 'color')
        
#create class for Canvas form
class CanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields =('title', 'description')
        

