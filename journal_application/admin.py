from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Notebook)
admin.site.register(Journal)
admin.site.register(Canvas)