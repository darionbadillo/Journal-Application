# Project-Application
Creating a journal application from the knowledge gained from my time in CS3300 at UCCS.

Links:

Github Repo: https://github.com/darionbadillo/Journal-Application
Kanban: https://github.com/users/darionbadillo/projects/2

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
`class Notebook(models.Model):`
    `title = models.CharField(max_length=200)`
    `about = models.CharField(max_length=1000, blank = True, default='')`
   ` private = models.BooleanField(default=False)`
    `color = models.CharField(max_length=10, choices=COLOR_CHOICES, default='black')   `
    `#Define default String to return the name for representing the Model object."`
    `def __str__(self):`
        `return self.title`
    `user = models.ForeignKey(User, on_delete=models.CASCADE, default = None)`
    `# Returns the URL to access a particular instance of MyModelName.`
   ` # if you define this method then Django will automatically`
    `# add a "View on Site" button to the model's record editing screens in the Admin site`
    `def get_absolute_url(self):`
        `return reverse('notebook-detail', args=[str(self.id)])`

In python, classes have certain attributes that define them. Here, a notebook contains `fields` for:
    - `title`
    - `about`
    - making the notebook `private` 
    - `color` choice. 

These are all callable attributes that the user will define upon creation of said notebook.

Notice how notebooks are tied to a specific user. Users can have multiple different notebooks that can contain multiple different journals and canvases.

# Views
Views are integral component that helps determine what content is displayed depending on the web request being sent.

## Detail Views
