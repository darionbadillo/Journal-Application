from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', 'first_name', 'last_name',]

admin.site.register(Notebook)
admin.site.register(Journal)
admin.site.register(Canvas)
