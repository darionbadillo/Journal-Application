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



### Editing

### Deleting


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
