The goal of this project is to return database response in the given format by developing a Django Project.

Usage:
pip install django
django-admin startproject ‘project-name’ create django project
cd ‘project-name’
python manage.py startapp ‘app-name’  creates an app in the project  a
pip freeze > requirements.txt  lists all the required libraries used 
Heroku Part
Install heroku by following instructions in the given url  https://devcenter.heroku.com/articles/getting-started-with-python#set-up
Setting up heroku can be done by following the link 
https://devcenter.heroku.com/articles/getting-started-with-python
Database Part
heroku run python manage.py migrate  runs migrations for the models.py 

Once everything is successful you can open the app from heroku platform.
This opens a new tab with the following url https://[appname].herokuapp.com/
