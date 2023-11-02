from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('users/', views.userListView.as_view(), name= 'users'),
    path('user/<int:pk>', views.userDetailView.as_view(), name='user-detail'),
    path('notebook/<int:pk>', views.notebookDetailView.as_view(), name='notebook-detail'),
    
    # Journal urls
    path('journals/', views.JournalListView.as_view(), name= 'journals'),
    path('journals/<int:pk>', views.JournalDetailView.as_view(), name='journal-detail'),
    path('notebook/<int:notebook_id>/create_journal/', views.createJournal, name='create_journal'),
    path('notebook/<int:notebook_id>/delete_journal/<int:journal_id>/', views.deleteJournal, name='delete_journal'),
    path('notebook/<int:notebook_id>/update_journal/<int:journal_id>/', views.updateJournal, name='update_journal'),
    
    # Canvas urls
    path('canvases/', views.CanvasListView.as_view(), name= 'canvases'),
    path('canvases/<int:pk>', views.JournalDetailView.as_view(), name='canvas-detail'),
    path('notebook/<int:notebook_id>/create_canvas/', views.createCanvas, name='create_canvas'),
    path('notebook/<int:notebook_id>/delete_canvas/<int:canvas_id>/', views.deleteCanvas, name='delete_canvas'),
    path('notebook/<int:notebook_id>/update_canvas/<int:canvas_id>/', views.updateCanvas, name='update_canvas'),
    
    # Notebook urls
    path('notebook/update_notebook/<int:student_id>/', views.updateNotebook, name='update_notebook'),
]
