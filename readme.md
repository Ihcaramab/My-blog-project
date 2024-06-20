requirements.txt (if you are hosting or want to send someone your project the person doesn't need to start downloading them again, the person just needs to go to your requirements.txt file and install the packages or libraries you have there.)
Creat your virtual environment.
Activate it.
Pip install django
Pip freeze > requirements.txt
django-admin startproject blog . (to avoid duplicate creation)
django-admin manage.py startapp core
Register the app
Go to views and define functions
Inside the core app, create a folder called templates
Inside the templates folder, create a folder called core
Inside the core folder, create an index.html file
Download your template and put in the html file
Run server
Connect your template to the main url(project url). If you don't connect your template to the main url, it won't show on your website.
Create a urls.py file in your app
Import path first (from django.urls import path)
Import views (from . import views, from .vies import homepage) (Read on MVC (Model Views Control), Algorithms)
Go to the main url and import include, then do this (path("", include("core.urls")),)
Include means you are trying to include another url from another app (stfn reloaded( the new camping, chinese, june 6))
Run server
Setup your static files
Copy your static folders from your template and go to your project folder and paste them there
Go to your settings and fix the path in the static area
Set up the root (which root is django going to get the staticfiles from)
Import OS
python manage.py collectstatic
Run server
Go to the index.html file and load static
Add static to all the static files
Run server
Setup your base.html
Go to your templates folder and create a base.html file
Go to your index.html file and extend base.html
Also load static
Go to your index.html file and copy the head section and paste it in your base.html file. Then go to the top and extend then add ({% block content}, {% endblock%})
Copy the footer section and paste it in the base.html file
The base contains any page that is going to be repeated often (Nav bar, footer)
Then add {% block content}, {% endblock%} to the middle of the header section and the footer section
Run server
Create another app
Go to views and define an about function (about.html)
Create an about.html file in the core folder in the templates folder
Go to the urls.py and import the aboutpage and add the path
Copy the about.html content and put it in your about.html file
Remove the header and the footer contents and add block content, load static and endblock content 
Go to the base.html and change the names of the files to the ones you have in the urls.py
Runserver
Go to views and define a product function (product.html)
Create a product.html file in the core folder in the templates folder
Go to the urls.py and import the productpage and add the path
Copy the product.html content and put it in your product.html file
Remove the header and the footer contents and add block content, load static and endblock content
Go to the base.html and change the names of the files to the one you have in the urls.py
Runserver
Go to views and define a blogg function (blogg.html)
Create a blogg.html file in the core folder in the templates folder
Go to the urls.py and import the bloggpage and add the path
Copy the blogg.html content and put it in your blogg.html file
Remove the header and the footer contents and add block content, load static and endblock content
Go to the base.html and change the names of the files to the one you have in the urls.py
Remember to add static to all the static files
Runserver
Go to views and define a contactus function (contactus.html)
Create a contactus.html file in the core folder in the templates folder
Go to the urls.py and import the contactuspage and add the path
Copy the contactus.html content and put it in your contactus.html file
Remove the header and the footer contents and add block content, load static and endblock content
Go to the base.html and change the names of the files to the one you have in the urls.py
Runserver



Blog project
Apps in the blog project
=> Core
    homepage
    about
    contact
=> Products
    creating of product models
    setting up the product admins, views and htmls