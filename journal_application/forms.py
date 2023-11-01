from django.forms import ModelForm
from .models import *

#create class for project form
class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields =('title', 'description')
        
#create class for notebook form
class NotebookForm(ModelForm):
    class Meta:
        model = Notebook
        fields =('title', 'user_email', 'about')
        
#create class for Canvas form
class CanvasForm(ModelForm):
    class Meta:
        model = Canvas
        fields =('title', 'description')
