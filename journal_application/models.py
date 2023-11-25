from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
  
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
]

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField("Email", max_length=200, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = None
        super(User, self).save(*args, **kwargs)

    
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

