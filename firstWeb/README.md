## Lessons Learned 🏍

Django is a framework written in Python. A Django project is a collection of different applications having different functionalities.
It allows to map a requested URL from a user to the code that is actually meant to handle it. 
With the use of templates we can inject calculated values or information from a database into a HTML page.
This framework connects the front-end with the back-end.

*Note: A web framework is a collection of modular tools that abstracts away much of the difficulty and repetition of web development. 
I.e: Django & Flask in Python, Rails in Ruby, and Express in JavaScript.*

        django-admin startproject project_name

The above command starts a new project. Inside this project we will have a directory (with the same name as project_name) and a manage.py file.
Inside the directory we will find 4 files:

- A blank __init__.py file that lets python know that this directory should be treated as a package.
- A settings.py file where all the project settings will be stored.
- An urls.py file to save al the URL pattern for the project and the different pages of the application.
- A wsgi.py file that acts as the web server Gateway interface helping us to stage the project later.

To start a new App in Django:
        
        python manage.py startapp app_name

This app will carry some files as well:

- __init__.py which function the same way as explained above.
- admin.py where you register your models to use them with Django's admin interface
- apps.py where we can place specific configurations of the application
- models.py where we are going to store our data models and specify the entities and relationships between the data.
- test.py which is used to save different functions to test our app.
- views.py which handles the requests and return the responses.
- A 'migrations' folder that stores database and it's specific information as it relates to the models.

Everything you can see in Django is a view. When we create a view in app_name/views.py is important to **map it** to app_name/urls.py. This is all done using the files within the app.
Later we need to use the urls.py of the Django project (djangoProject/urls.py) and map the URL file of our app here.

### Models

A model is a source of information about our data. It contains behavioural aspects and other essential features of our data. These are a way to create a database for a Django project.
Is important to note that each models maps to a single database table and you can check the default database you are using in the settings.py file of your project.

    DATABASES = {
        'default': {
            'ENGINE':
    'django.db.backends.sqlite3',
            'NAME':
    os.path.join(BASE_DIR,
    'db.sqlite3'),
        }
    }

Inside this same file we can see the INSTALLED_APPS, where some of these apps use at least one database, so to create a table run in the terminal:

        python manage.py migrate

This command will look at the INSTALLED_APPS and create the necessary tables.

#### Create a Model

To create a model, it is done in app_name/models.py 

        class Example(models.Model):
            attribute_1 = models.Charfield(max_length= 50)
            ...

            def __str__(self):
                return self.attribute_X

We can create ad many models as we want and they will inherit they features form *models.Model*. The attributes show in the example above will be the columns of the table.
Note: we can associate models using *models.ForeignKey(class_name, on_delete = models.CASCADE)*, i.e. Also, it is important to add a __str__ method.

#### Activate Models

Once we create the model we need to add the app configuration into the INSTALLED_APPS:

        INSTALLED_APPS=[ 
            ..., 
            'app_name', 
        ]

Once this is done, on the terminal:
        
        python manage.py makemigrations app_name

When we use this command we tell python we have added a new model or made changes into the existing ones. This will create a Python database-access API for accessing the models objects.
Finally, to create those tables in our database we use the *python manage.py migrate* command again. We have to use this two commands whenever we create a new model or changed something in the existing one.

### Admin user

Django automates the creating of an admin interface models. To create an administrator user run in the terminal:

    python manage.py createsuperuser

It will ask you the Username, Email & Password. Don't lose it.
To see the created models in the admin site, inside the app_name/admin.py add:

    from django.contrib import admin
    from .models import Model_name
    
    admin.site.register(Model_name)

This way you can edit, add and delete the model information (the database info) from the administration panel.


### Templates

It is used to tag and implement various logics from an HTML file to python. There are 2 types of templates:

1) {{ variable }} which is used for different variables.
2) {% logics %}, used to put logic, loops and links.

Create a template folder in the app and inside this folder create another folder with the app_name. Finally, add an index.html file into the last folder.
This template is used in app_name/views.py to create the views, and then we will have to follow the steps above (to map it to urls and stuff).


Bootstrap es un Framework CSS creado por twitter en el 2011, este sirve para dar un formato a un sitio web usando librerías css.
La principal característica de este framework es que es 'responsive' (a.k.a: se ve perfectamente en cualquier dispositivo).
Otra ventaja es que es compatible con la mayoría de los navegadores, además de aportar rapidez al diseño web y permitir el uso de LESS.

Se puede usar el panel de administración para manejar las aplicaciones creadas. Aunque es necesario configurar Django para poder guardar datos en la base de dato y para mostrarlos en la página web.

