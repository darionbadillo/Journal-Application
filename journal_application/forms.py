from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')  
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
