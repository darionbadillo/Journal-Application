from typing import Any
from django.shortcuts import *
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *
    
# Create your views here.
def index(request):
    all_notebooks = Notebook.objects.all()
    return render( request, 'journal_application/index.html', {'all_notebooks': all_notebooks})

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
    return render(request, 'journal_application/Notebook_form.html', context)


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
def deleteJournal(request, Journal_id, notebook_id):
    # Gets the Journal to delete
    Journal = get_object_or_404(Journal, pk=Journal_id)
    
    # Deletes the Journal if the request method is POST
    if request.method == 'POST':
        Journal.delete()
        return redirect('notebook-detail', notebook_id)

    # Renders the delete Journal page
    context = {'Journal': Journal}
    return render(request, 'journal_application/delete_Journal.html', context)

#Updates an existing journal
def updateJournal(request, notebook_id, Journal_id):
    Journal = get_object_or_404(Journal, pk=Journal_id)
    
    form = JournalForm(instance=Journal)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=Journal)
        if form.is_valid():
            form.save()
            return redirect('notebook-detail', notebook_id)
        
    context = {'form': form, 'notebook_id': notebook_id, 'Journal': Journal} 
    return render(request, 'journal_application/update_Journal.html', context)

#Creates a new Canvas
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
def deleteCanvas(request, Canvas_id, notebook_id):
    # Gets the Journal to delete
    Journal = get_object_or_404(Journal, pk=Canvas_id)
    
    # Deletes the Journal if the request method is POST
    if request.method == 'POST':
        Canvas.delete()
        return redirect('notebook-detail', notebook_id)

    # Renders the delete Journal page
    context = {'Canvas': Canvas}
    return render(request, 'journal_application/delete_Journal.html', context)

#Updates an existing journal
def updateCanvas(request, notebook_id, Canvas_id):
    Canvas = get_object_or_404(Canvas, pk=Canvas_id)
    
    form = JournalForm(instance=Journal)
    if request.method == 'POST':
        form = CanvasForm(request.POST, instance=Canvas)
        if form.is_valid():
            form.save()
            return redirect('notebook-detail', notebook_id)
        
    context = {'form': form, 'notebook_id': notebook_id, 'Canvas': Canvas} 
    return render(request, 'journal_application/update_Canvas.html', context)

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