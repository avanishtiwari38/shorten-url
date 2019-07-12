## Installation

1.Create a python 3 environment. All the dependencies of a project should be ported in a Venv
    
    virtualenv -p python3 envname

2.Switch to that environment 
    
    source path-to-env/envname/bin/activate
    
    PS - Install virtualenvwrapper to make the virtual env process easier
    
3.Install requirements from `requirements.txt`. 

Use the requirement files for each environment to install all the requirements in a single step using `pip install -r requirements/requirements.txt`

4.Edit config file as per your database.
    
    cd inside the config folder
    cd config
    vim local_config.py
     
5.Run flask migrations 


NOTE - DB `shorten_url` should be created manually in postgres


Initialise the db `flask db init`, this would setup a migration directory structure.
It is not required it if already exists in the project.

To create a migration use `flask db migrate` this will pick up the model changes from models.py and create a db script for postgres

To apply already created migrations to the db using `flask db upgrade`. This will push the changes to the DB. This should be the only command needed in production.  

6.Run flask server

    python run.py