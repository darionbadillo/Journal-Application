from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    #path('users/', views.userListView.as_view(), name= 'users'),
    #path('user/<int:pk>', views.userDetailView.as_view(), name='user-detail'),

    # Journal urls
    path('journals/', views.JournalListView.as_view(), name= 'journals'),
    path('journals/<int:pk>', views.JournalDetailView.as_view(), name='journal-detail'),
    path('notebook/<int:notebook_id>/create_journal/', views.createJournal, name='create_journal'),
    path('notebook/<int:notebook_id>/delete_journal/<int:journal_id>/', views.deleteJournal, name='delete_journal'),
    path('notebook/<int:notebook_id>/update_journal/<int:journal_id>/', views.updateJournal, name='update_journal'),
    
    # Canvas urls
    path('canvases/', views.CanvasListView.as_view(), name= 'canvases'),
    path('canvases/<int:pk>', views.CanvasDetailView.as_view(), name='canvas-detail'),
    path('notebook/<int:notebook_id>/create_canvas/', views.createCanvas, name='create_canvas'),
    path('notebook/<int:notebook_id>/delete_canvas/<int:canvas_id>/', views.deleteCanvas, name='delete_canvas'),
    path('notebook/<int:notebook_id>/update_canvas/<int:canvas_id>/', views.updateCanvas, name='update_canvas'),
    
    # Notebook urls
    path('notebook/<int:pk>', views.notebookDetailView.as_view(), name='notebook-detail'),
    path('notebook/create_notebook', views.createNotebook, name='create_notebook'),
    path('notebook/update_notebook/<int:notebook_id>/', views.updateNotebook, name='update_notebook'),
    path('notebook/<int:notebook_id>/delete_notebook', views.deleteNotebook, name='delete_notebook'),
    
    # TinyMCE urls
    path('tinymce/', include('tinymce.urls')),
    
    # User Authentication urls
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),    
    path('registration/signup/', views.signup_view, name='signup'),
]
