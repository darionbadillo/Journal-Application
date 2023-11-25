from typing import Any
from django.shortcuts import *
from django.http import *
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
    
# Home page view
def index(request):
    all_notebooks = Notebook.objects.all()
    return render( request, 'journal_application/index.html', {'all_notebooks': all_notebooks})

# Notebook views

# Creates a new Notebook
def createNotebook(request):
    form = NotebookForm()
    
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            # Save the form to create a Notebook instance
            notebook = form.save()
            notebook.save()
            # Redirect back to the notebook detail page
            return redirect('notebook-detail', notebook.id)

    context = {'form': form}
    return render(request, 'journal_application/notebook_form.html', context)

def updateNotebook(request, notebook_id):
    
    notebook = Notebook.objects.get(id=notebook_id)    
    
    form = NotebookForm(instance=notebook)
    if request.method == 'POST':
        form = NotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            form.save()
            return redirect('notebook-detail', notebook_id)
        
    context = {'form': form, 'notebook': notebook} 
    return render(request, 'journal_application/update_notebook.html', context)

def deleteNotebook(request, notebook_id):
    # Gets the Journal to delete
    notebook = get_object_or_404(Notebook, pk=notebook_id)
    
    # Deletes the Journal if the request method is POST
    if request.method == 'POST':
        notebook.delete()
        return redirect('/')

    # Renders the delete Journal page
    context = {'Notebook': notebook}
    return render(request, 'journal_application/delete_Notebook.html', context)

# Journal views

# Creates a new Journal
def createJournal(request, notebook_id):
    form = JournalForm()
    notebook = Notebook.objects.get(pk=notebook_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and notebook_id
        Journal_data = request.POST.copy()
        Journal_data['notebook_id'] = notebook_id
        
        form = JournalForm(Journal_data)
        if form.is_valid():
            # Save the form without committing to the database
            Journal = form.save(commit=False)
            # Set the notebook relationship
            Journal.notebook = notebook
            Journal.save()

            # Redirect back to the notebook detail page
            return redirect('notebook-detail', notebook_id)

    context = {'form': form}
    return render(request, 'journal_application/Journal_form.html', context)

# Deletes Journals
def deleteJournal(request, journal_id, notebook_id):
    # Gets the Journal to delete
    journal = get_object_or_404(Journal, pk=journal_id)
    
    # Deletes the Journal if the request method is POST
    if request.method == 'POST':
        journal.delete()
        return redirect('notebook-detail', notebook_id)

    # Renders the delete Journal page
    context = {'Journal': journal}
    return render(request, 'journal_application/delete_Journal.html', context)

#Updates an existing journal
def updateJournal(request, notebook_id, journal_id):
    journal = get_object_or_404(Journal, pk=journal_id)
    
    form = JournalForm(instance=journal)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save()
            return redirect('notebook-detail', notebook_id)
        
    context = {'form': form, 'notebook_id': notebook_id, 'Journal': journal} 
    return render(request, 'journal_application/update_journal.html', context)


# Canvas views

# Creates a new Canvas
def createCanvas(request, notebook_id):
    form = CanvasForm()
    notebook = Notebook.objects.get(pk=notebook_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and notebook_id
        Canvas_data = request.POST.copy()
        Canvas_data['notebook_id'] = notebook_id
        
        form = CanvasForm(Canvas_data)
        if form.is_valid():
            # Save the form without committing to the database
            Canvas = form.save(commit=False)
            # Set the notebook relationship
            Canvas.notebook = notebook
            Canvas.save()

            # Redirect back to the notebook detail page
            return redirect('notebook-detail', notebook_id)

    context = {'form': form}
    return render(request, 'journal_application/Canvas_form.html', context)

# Deletes Journals
def deleteCanvas(request, canvas_id, notebook_id):
    # Gets the Journal to delete
    canvas = get_object_or_404(Canvas, pk=canvas_id)
    
    # Deletes the Journal if the request method is POST
    if request.method == 'POST':
        canvas.delete()
        return redirect('notebook-detail', notebook_id)

    # Renders the delete Journal page
    context = {'Canvas': canvas}
    return render(request, 'journal_application/delete_Canvas.html', context)

#Updates an existing journal
def updateCanvas(request, notebook_id, canvas_id):
    canvas = get_object_or_404(Canvas, pk=canvas_id)
    
    form = CanvasForm(instance=canvas)
    if request.method == 'POST':
        form = CanvasForm(request.POST, instance=canvas)
        if form.is_valid():
            form.save()
            return redirect('notebook-detail', notebook_id)
        
    context = {'form': form, 'notebook_id': notebook_id, 'Canvas': canvas} 
    return render(request, 'journal_application/update_Canvas.html', context)


#Lists and Details generic views
# Will activate when users are ready
""" class userListView(generic.ListView):
    model = User
class userDetailView(generic.DetailView):
    model = User """

class notebookDetailView(generic.DetailView):
    model = Notebook 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_list'] = Journal.objects.all()
        context['canvas_list'] = Canvas.objects.all()
        return context

class JournalListView(generic.ListView):
    model = Journal
class JournalDetailView(generic.DetailView):
    model = Journal

class CanvasListView(generic.ListView):
    model = Canvas
class CanvasDetailView(generic.DetailView):
    model = Canvas
    
def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to a home page
    else:
        form = UserCreationForm()
    return render(request, 'journal_application/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally log the user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to a home page