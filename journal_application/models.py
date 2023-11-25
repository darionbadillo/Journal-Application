from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.conf import settings
  
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
    
class Notebook(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=1000, blank=True, default='')
    private = models.BooleanField(default=False)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')   
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notebook-detail', args=[str(self.id)])  

class Journal(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=False, default='')
    content = HTMLField(blank=True, default='')
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('journal-detail', args=[str(self.id)])

class Canvas(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=False, default='')
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('canvas-detail', args=[str(self.id)])
