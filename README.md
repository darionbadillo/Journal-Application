# Project-Application
Creating a journal application from the knowledge gained from my time in CS3300 at UCCS.

Links
## Welcome to the app

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


6. Begin coding! Please remember to branch your specific code
    - How to create a new git branch
        - `git checkout branch-name`
    - Commit frequently
        - `git status`
            - Checks all changes and what is currently being tracked
        - `git add --all`
        - `git commit -m "what youve done"`
    - Push to remote repo when done
        - `git push`



# Forms

# Dark Mode
