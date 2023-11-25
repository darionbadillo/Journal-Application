from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
  
COLOR_CHOICES = [
    ('red', 'Red'),
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('purple', 'Purple'),
    ('yellow', 'Yellow'),
    ('orange', 'Orange'),
    ('brown', 'Brown'),
    ('black', 'Black'),
    ('pink', 'Pink'),
    ('white', 'White')
]

# Cannot implement yet because we need are not implementing users yet
""" class User(models.Model):

    name = models.CharField(max_length=200)
    email = models.CharField("Email", max_length=200)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.name

    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)]) """
    
class Notebook(models.Model):
    
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=1000, blank = True, default='')
    private = models.BooleanField(default=False)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')   
    
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

    #user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('notebook-detail', args=[str(self.id)])  
    
class Journal(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank = False, default='')
    content = HTMLField(blank = True, default='')
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default = None)
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('journal-detail', args=[str(self.id)])
    

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank = False, default='')
    
    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title

    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default = None)
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('canvas-detail', args=[str(self.id)])

