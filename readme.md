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
Import views (from . import views, from .vies import homepage) (Read on MVC (Model Views Control), Algorithms, ORM (Object Relational Mapping))
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
Create another app and call it products
Go and register it in the settings
Go to models.py and type "from django.contrib.auth.models import User"
Django has created a model for user already so you don't to start creating it again. All you have to do is to import it
Add it in your product
Then add a class
Whenever you are using a CharField in django, always specify the number of characters you want the user to input(max_length)
When using slug, you don't need space. Slug(8000/blog/detail/my-shoe)
Create your category models
Create your product models
Then take everything to your database(python manage.py makemigrations)
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
To register models, go to the products app, then go to admin.py and import Product, Category
admin.site.register(Product)
To upload images to media, you have to install pillows
pip install pillow
pip freeze > requirements.txt
Whenever you make any changes, you must always makemigrations and migrate
Delete the 0001init_py and the dbsqlite
Go to each of the fields in your models.py and add null=True, blank=True
Makemigrations and migrate
Createsuperuser
Runserver
Click on add products, then click on add category(name=cat1, slug=cat-1, date=today and time=now) then save
Click on add products, choose a category, specify the user, give it a name, slug, description, price and image then save
pip install python-slugify
Whenever you download something in django, always do (pip freeze > requirements.txt)
Go to your models.py and import slugify then do (
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
            )
You use args and kwargs when you want to add unspecified parameters. With the args and kwargs(keyword args), it can accept any parameters it wants to accept
Runserver
When you want to add another category, you can go ahead and ignore the slug and just put your descriptions
Update your codes to github




Blog project
Apps in the blog project
=> Core
    homepage
    about
    contact
=> Products
    creating of product models
    setting up the product admins, views and htmls