System Requirements

python (3.7.2) -> (Required) Python is required for this project
pip (20.0.2) -> (Required) Pip is required to install python dependencies
django -> The outlining REST framework to run our server, interact with the DB and serve up our data models to the client.
djangoRestFramework- to run our  api

Install Steps:

1. download 
2.We need to migrate the built in models to our database.
  run command: python manage.py migrate
3.If you have added models of your own you need migrate those models with

      python manage.py makemigrations
 4.Create Super User

      python manage.py createsuperuser

      Username (leave blank to use 'zingsoft'): 
      Email address: example@example.com
      Password: 
      Password (again): 
      Superuser created successfully.
  
 5.Create Some Records

    We need to add some records to our hero table. We can do that by starting the server and adding them.

    python manage.py runserver
