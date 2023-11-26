# Project-Application
Creating a journal application from the knowledge gained from my time in CS3300 at UCCS.

Links:

[Github Repo](https://github.com/darionbadillo/Journal-Application)

[Kanban](https://github.com/users/darionbadillo/projects/2)

## Welcome to the app
Welcome to the Notebooking app. 

# Base Environment Set Up
The base environment is set up utilizing your command line. 

1. Open command line
2. Create a local repository to store the code you're working on from this repo
    1. `mkdir repos`
    2. `cd repos`
    3. `mkdir journal`
    4. `cd journal`
    5. `git init`
    6. `git clone https://github.com/darionbadillo/Journal-Application.git`

3. You will need these three commands for the command line to get your server running every time. Multiple Command Prompt windows will be needed.
    - `cd C:\Your\Location\repos\journal`
        - This is only used if you're not currently in the required directory.
    - `djvenv\Scripts\activate`
        - This activates your virtual environment for python coding

4. Now that you're in your virtual environment, install all requirements
    - `pip install -r requirements.txt`

5. Once it is done, activate the server.
    - `py manage.py runserver`
    - Type in "http://localhost:8000 into your browser and you will see the homepage for our application

6. Begin coding! Please remember to branch your specific code
    - How to create a new git branch
        - `git checkout branch-name`
    - Commit frequently
        - `git status`
            - Checks all changes and what is currently being tracked
        - `git add --all`
            - adds all changes that have been made
        - `git commit -m "what youve done"`
            - commits all files locally. All commits have a name and allow you to backtrack if anything goes wrong.
    - Push to remote repo when done
        - `git push`


# Models
Here is an example of how a model is crafted in Django
Models are essential for created classes. In this application, we have Notebooks, Journals, Canvases, and Users.

Notebook Model:

```
class Notebook(models.Model):
    title = models.CharField(max_length=200)
    about = models.CharField(max_length=1000, blank = True, default='')
    private = models.BooleanField(default=False)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')
    def __str__(self):
        return self.title
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    
    def get_absolute_url(self):
        return reverse('notebook-detail', args=[str(self.id)])
```


In python, classes have certain attributes that define them. Here, a notebook contains `fields` for:
- `title`
- `about`
- making the notebook `private` 
- `color` choice. 

These are all callable attributes that the user will define upon creation of said notebook.

Notice how notebooks are tied to a specific user. Users can have multiple different notebooks that can contain multiple different journals and canvases.


# Templates, and Forms
We will be using the Notebook model from the Models section as an example.
## Creating
- Using the Notebook model, we would then need to create a `form` for essentially almost all dealings with user based input

**Notebook Form**
```class NotebookForm(ModelForm):
    class Meta:
        model = Notebook
        fields =('title', 'about', 'color')
```
- Notice the fields detail out all the attributes from the model
- Create a new view in views.py

**Create Notebook View**
```
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
```

**Breakdown of Code**
- `form = NotebookForm()`:
    - A new, empty instance of NotebookForm is created. This will be used to display an empty form on the webpage.

- `if request.method == 'POST'`:
    - This checks if the current request is a POST request, which generally means the form has been submitted.

- `form = NotebookForm(request.POST)`:
    - If the form has been submitted, a new instance of NotebookForm is created using the data from the POST request.

- `if form.is_valid():`:
    - Checks if the data from the form meets all validation criteria (e.g., required fields, data types, etc.).

- `notebook = form.save()`:
    - If the form data is valid, the data is saved to create a new Notebook instance in the database.

- `notebook.save()`:
    - Saves the Notebook instance to the database. However, this line is redundant since form.save() already commits the instance to the database, unless the commit argument is set to False.

- `return redirect('notebook-detail', notebook.id)`:
    - After the new notebook is saved, the user is redirected to its detail page. The notebook-detail view is expected to show details of a specific notebook, and it requires the ID of the notebook as an argument.

- `context = {'form': form}`:
    - Creates a dictionary that holds the form instance. This context is passed to the template, allowing it to be rendered on the webpage.

- `return render(request, 'journal_application/notebook_form.html', context)`:
    - Renders the notebook_form.html template. This is the page where the user will see and interact with the form. The context passed ensures the form is displayed

**Template Creation**
- Next is the creation of a html template pages
- We will need to create a detail, and form template.

**notebook_detail.html**
```
{% extends 'journal_application/base_template.html' %}
{% block content %}
<div class="container mt-5">
    <div class="card shadow">
        <div class="card-body">
            <h2 class="card-title">Create New Notebook</h2>
            <form action="" method="POST" class="mt-3">
                {% csrf_token %}
                {% for field in form %}
                <div class="mb-3">
                    <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
                    {# This will render the dropdown if the option is necessary#}
                    {% if field.field.widget.input_type == 'select' %}
                    {{ field }}
                    {% else %}
                    <input type="{{ field.field.widget.input_type }}" name="{{ field.name }}" class="form-control"
                        id="{{ field.auto_id }}" value="{{ field.value|default:'' }}"
                        placeholder="{{ field.help_text|default:'' }}">
                    {% endif %}
                </div>
                {% endfor %}
                <div class="mt-auto">
                    <button type="submit" class="btn btn-primary">Submit</button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```
- This is absolutely NECESSARY to create any new notebooks. 

**Breakdown of HTML code**
- {% extends 'journal_application/base_template.html' %}:
    - This template inherits from a base template (base_template.html). This allows for consistent design and layout across different pages of the website.

- {% block content %}...{% endblock %}:
    - The content between these tags is meant to override the content block in the base template. This is the main content of this particular page.

- <div class="container mt-5">...:
    - The main content is wrapped inside a container class (a Bootstrap class) with a top margin. This ensures appropriate spacing and alignment.

- <div class="card shadow">:
    - The form is wrapped inside a Bootstrap card component. The shadow class gives a shadow effect to the card, enhancing its visual appeal.

- <form action="" method="POST" class="mt-3">:
    - This starts the form declaration. The form uses the POST method to submit data.

- {% csrf_token %}:
    - This template tag outputs a CSRF token, which is essential for security in Django forms to prevent cross-site request  forgery attacks.

- {% for field in form %}...{% endfor %}:
    - This loop iterates over each field in the form. For every field, it renders the appropriate input component, be it a text box, dropdown, etc.

- {% if field.field.widget.input_type == 'select' %}:
    - This conditional checks if the field's widget type is 'select'. If it is, it renders the field directly, ensuring a dropdown is shown.

- <input type="{{ field.field.widget.input_type }}" ... >:
    - If the field is not a select dropdown, an input of the appropriate type is rendered. The type, name, ID, and value are dynamically set based on the field's properties.

- <button type="submit" class="btn btn-primary">Submit</button>:
    - This is the submit button for the form. Once clicked, the form's data is submitted for processing.

**URL**
- Make sure to create a URL path inside the urls.py
    - `path('notebook/create_notebook', views.createNotebook, name='create_notebook'),`

### Editing
Editing a model is much easier.

**UpdateNotebook View**
1. The function retrieves the notebook to be updated based on the provided `notebook_id`.
2. An instance of the `NotebookForm` is created with the retrieved notebook's data as its initial values.
3. If the form is submitted using a POST request, the data is validated, the notebook is updated, and the user is redirected to the notebook's detail page.
4. If the form is not submitted or there are validation errors, the form is displayed to the user for editing.

```
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

```

**Code Breakdown**

- `def updateNotebook(request, notebook_id):`:
  - Defines the function with two parameters: the `request` object and the `notebook_id` of the notebook to be updated.

- `notebook = Notebook.objects.get(id=notebook_id)`:
  - Fetches the notebook with the given `notebook_id` from the database.

- `form = NotebookForm(instance=notebook)`:
  - Initializes the `NotebookForm` with the data from the fetched notebook.

- `if request.method == 'POST':`:
  - Checks if the request is a POST request, which indicates that the form has been submitted for updating.

- `form = NotebookForm(request.POST, instance=notebook)`:
  - Binds the submitted POST data to the `NotebookForm`, while still associating it with the original notebook instance.

- `if form.is_valid():`:
  - Validates the form data. If all fields contain valid data:

    - `form.save()`: Saves the updated notebook to the database.
    
    - `return redirect('notebook-detail', notebook_id)`: Redirects the user to the detail view of the updated notebook.

- `context = {'form': form, 'notebook': notebook}`:
  - Prepares the context data to be passed to the template. This includes both the form and the notebook instance.

- `return render(request, 'journal_application/update_notebook.html', context)`:
  - Renders the `update_notebook.html` template with the prepared context. This will display the form to the user, allowing them to make edits to the notebook.

**update_notebook.html**
1. The template is built on top of a base template to maintain a consistent look and feel across the application.
2. A form is presented to the user, pre-filled with the existing details of a notebook.
3. Validation errors, if any, are displayed next to the respective input fields.
4. Upon submission, the form data is sent to the server for processing.

```
{% extends 'journal_application/base_template.html' %}

{% block content %}

<div class="container mt-5">
    <h2 class="mb-4">Update Notebook</h2>

    <form action="" method="POST" class="needs-validation" novalidate>
        {% csrf_token %}

        {% for field in form %}
        <div class="mb-3">
            <label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>
            {{ field.errors.as_text }}
            <!-- Display field errors -->
            {{ field }}
            <!-- This will render each field -->
        </div>
        {% endfor %}

        <div class="mt-4">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </form>
</div>

{% endblock %}
```

**Code Breakdown**

- `{% extends 'journal_application/base_template.html' %}`:
  - The template inherits from the `base_template.html` to maintain a consistent structure and design.

- `{% block content %}`:
  - This block defines the main content of the page, which will replace the corresponding block in the base template.

- `<div class="container mt-5">`:
  - Creates a container with a top margin for styling purposes.

- `<h2 class="mb-4">Update Notebook</h2>`:
  - Displays the heading "Update Notebook".

- `<form action="" method="POST" class="needs-validation" novalidate>`:
  - Begins the form with a POST method. The `needs-validation` and `novalidate` attributes are used for client-side form validation.

- `{% csrf_token %}`:
  - Inserts a CSRF token into the form for security purposes, which helps prevent Cross-Site Request Forgery attacks.

- `{% for field in form %}`:
  - Iterates over each field in the provided form.

    - `<label for="{{ field.id_for_label }}" class="form-label">{{ field.label }}</label>`:
      - Renders a label for the current form field.

    - `{{ field.errors.as_text }}`:
      - If there are validation errors for the current field, they are displayed in text format.

    - `{{ field }}`:
      - Renders the actual input element for the current field.

- `<button type="submit" class="btn btn-primary">Submit</button>`:
  - Creates a submit button for the form. When clicked, the form data will be sent to the server for processing.

**URL**
- `path('notebook/update_notebook/<int:notebook_id>/', views.updateNotebook, name='update_notebook'),`


### Deleting

**deleteJournal View**
1. The function retrieves a notebook based on its unique ID.
2. If the user confirms the deletion (via a POST request), the notebook is deleted.
3. The user is redirected to the home page after deletion.
4. If the user lands on the page via a GET request, they are presented with a confirmation page for deletion.

```
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
```

**Code Breakdown**

- `def deleteNotebook(request, notebook_id):`:
  - Defines the view function, accepting the request object and the unique ID of the notebook to delete.

- `notebook = get_object_or_404(Notebook, pk=notebook_id)`:
  - Tries to retrieve the notebook with the given ID (`notebook_id`). If it doesn't exist, the function will return a 404 Not Found response.

- `if request.method == 'POST':`:
  - Checks if the current request is a POST request (i.e., the user has confirmed the deletion).

    - `notebook.delete()`:
      - Deletes the notebook from the database.

    - `return redirect('/')`:
      - Redirects the user to the home page (root URL) after successful deletion.

- `context = {'Notebook': notebook}`:
  - Prepares the context to be passed to the template. This allows the template to display details about the notebook that's about to be deleted, so the user knows exactly what they're confirming.

- `return render(request, 'journal_application/delete_Notebook.html', context)`:
  - Renders the `delete_Notebook.html` template, providing it with the context. This will show the user a confirmation page to ensure they genuinely want to delete the notebook.

**delete_notebook.html**
```
{% extends 'journal_application/base_template.html' %}

{% block content %}
<div class="container mt-5">
    <h1 class="display-4 mb-4">Delete Notebook</h1>

    <div class="alert alert-warning" role="alert">
        <h4 class="alert-heading">Warning!</h4>
        <p>Are you sure you want to delete this notebook? This action cannot be undone.</p>
        <hr>
        <p class="mb-0"><strong>Notebook Title:</strong> {{ Notebook.title }}</p>

        {# Iterates through all journals and canvases for display. Displays a message if no canvases or journals exist #}
        <p class="mb-0 mt-3"><strong>Journals in this Notebook:</strong></p>
        <ul>
            {% for journal in Notebook.journal_set.all %}
            <li>{{ journal.title }}</li>
            {% empty %}
            <li>No journals in this notebook.</li>
            {% endfor %}
        </ul>


        <p class="mb-0 mt-3"><strong>Canvases in this Notebook:</strong></p>
        <ul>
            {% for canvas in Notebook.canvas_set.all %}
            <li>{{ canvas.title }}</li>
            {% empty %}
            <li>No canvases in this notebook.</li>
            {% endfor %}
        </ul>

    </div>

    <form method="post">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger mb-3">Delete</button>
    </form>

    <a role="button" href="{{ Notebook.get_absolute_url }}" class="btn btn-secondary">Cancel</a>
</div>
{% endblock %}
```

- This HTML code lists the Notebook and all of its contents for the user while asking if they're sure they want to delete the notebook or not


**URL**
- `path('notebook/<int:notebook_id>/delete_notebook', views.deleteNotebook, name='delete_notebook'),`

# Views
Views are integral component that helps determine what content is displayed depending on the web request being sent.
We are utilizing two generic type views called DetailViews and ListViews.
- These allow for Simplicity, Reusability, and overall Consistency in our application. 
### DetailViews
**Purpose**
- Essential for displaying a singular item. 
- We will be using DetailViews to see all Notebooks, Journals, Canvases, and User information
**Example**
```
class notebookDetailView(generic.DetailView):
    model = Notebook 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_list'] = Journal.objects.all()
        context['canvas_list'] = Canvas.objects.all()
        return context
```
- Here we are using a tying the attribute `model` to an instance of a `Journal`. 
- We can also see that Notebooks are tied together with a list of Journals and Canvases

### ListViews
**Purpose**
- Used for dislplaying a list of items.
- For example, we would use a list view to display ALL of the journals, or notebooks.
**Example**
```
class JournalListView(generic.ListView):
    model = Journal
```
