**-------------------------------MODULE - 1. DJANGO -------------------------------------- **

Django : 
- Django is a python framework that makes it easier to create the websites using python
- Django takes care of the difficult stuff such that we can concentrate on building our web app
- Django emphasizes the reusability off components that follows DRY( Donot Repeat Yourself), and comes with Ready to use features like login system, database connection and CRUD operations (Create Read Update and Delete) 


Working :
It follows the MVT Design ( Model ,View and Template)

a. Model : The data you want to present, usually data from a database.
b. View : A request handler that returns the relevant template and content template and content-based on the request from the user.
c. Template : A text file (like HTML file) containing the layout of the webpage, with logic on how to display the data.

Model :
- Provides data from Database.
- The data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.
- ORM makes Django easier to communicate with database, without having to write complex SQL statements.
- The models are usually located in models.py

View : 
- A function or method that takes http requests as arguments, imports the relevant model and finds out what data to send to the template and returns the final result.
- The views are usually located in a file called views.py

Template :
- A template is a file where you describe how the result should represented.
- Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files
- Templates of an app is located in the folder named templates

URLs : 
Django also provides a way to navigate around different pages in a website.
When a user requests a URL, Django decides which view it will send it to.
This is done in a file called urls.py


Internal Process:
When Django is installed and created your first django web app, and the browser requests the URL:

- Django recieves the URL, checks the urls.py file and calls the view that matches the URL.
- The view, located in views.py, checks for relevant models.
- The models are imported from models.py file
- The view send the data to a specified template in the template folder.
- The template contains the HTML and Django tags, and with the data it returns finished HTML content back to the browser.

* Make sure That python and pip package manager are installed in the system.
* For every django project, there should be different virtual environments.


Creating Virtual Environment : 
- In windows prompt, Run the following command
py -m venv my-practice

- Activate the environment, by typing :
my-practice\Scripts\activate.bat

- To deactivate the environment:
my-practice\Scripts\deactivate.bat

* Make sure that you activate the virtual environment everytime you open the cmd prompt


Installing DJANGO :
- To install Django, run the following Command : 
pip install django
- To check the django version : django-admin --version


Creating First Project :
- Go to the directory where you want to create django-project, Let us start the project using :
django-admin startproject first_project

- We get the folder with some files like :
manage.py
first_project:
	__init__.py
	asgi.py
	settings.py
	urls.py
	wsgi.py
 
- For Running the Django Project, we have to go to that folder and execute the commad:
py manage.py runserver


Create App:
- An App is a web based application that has a specific meaning in your project, like a home page, a contact form, or a members database.
- An app will be created to list and register members in the database.

- Initially, Let us create a simple project that displays "Hello World..!"
py manage.py startapp members

Then we get the structure:
members/
	migrations/
        	    __init__.py
	__init__.py
	admin.py
	apps.py
	models.py
        tests.py
	views.py

First let us go to Views.py, because this is where we need to send back a proper response.


Views: 
- Django views are python functions that takes the http requests and returns http response, like HTML documents
- A webpage that uses Django is full of views with different tasks and missions
- Views are usually put in a file called views.py located on your app's folder.
- There is a views.py in 'members' folder.

Let us write the content like this in views.py:

from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

In order to execute the above view, we must call the view via a URL


URLs:
- We need to create a file with name 'urls.py' in the same folder as the views.py file and type:

from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]

- The urls.py we have created is specific for members application. We have to do some routing in the root directory as well.
- Right now, Let is go to first-project folder, open the urls.py file and add the include module in the import statement, and also add a path() in urlspattern[] list, with arguments that will route users that comes in via localhost path.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
# Run the server


Templates:
- As we learned that the result should be in html, and it should be created in a template, so let us do that.
- Create a templates folder inside the members folder, and create a HTML file named myfirst.html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hello World!</h1>
        <p>Welcome to the first DJANGO project</p>
    </body>
</html>

- Now we have to modify the views.py and replace members with :
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

- Inorder to work with more complicated stuff than "Hello World", we have to tell Django that a new app is created.
- This is done in settings.py in the folder, There look up for the installed apps[] list and add the members app like this:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
]

After that migrate by runing the below command : 
py manage.py migrate


Models :
- A Django model is a table in the database
- Now let us see Django allows us to work with data without having to change or upload files in the process.
- In Django, data is created in objects, called models, and is actually tables in a database.

Create Table : 
- To create a model, navigate to the models.py file in the /members/ folder.
- Open it and add the member table by creating a Member class, and describe the table fields in it:
from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
- Here we have created two fields: firstName and lastname for our table. 
- Tables are stored in a database with file name db.sqlite3 (that was created at the time of creating the root folder first-project)
- By default, All the models created in the django project will be created as tables in the database

Migrate:
- After we have described a model in the models.py file, we must run a command to actually create the table in the database. Navigate to the folder :
py manage.py makemigrations members
- Then we will find a file created in the members / migrations/ 0001_initial.py
(There another primary key named id will be automatically of serial datatype by default)
- The model is created. Inorder to create the table, we need to run another command, such that django will create and execute an SQL statement, based on the content of the new file in the /migrations/ folder:
py manage.py migrate
- Now we have member table in the database

View SQL:
- We can view the SQL statement that were executed from the migration above.
- Run the command with the migration number:
py manage.py sqlmigrate members 0001


Insert Data:
- The members table is empty. We use the python interpreter to add some members to it.
To open python shell:	py manage.py shell

Let us write the piece of code to look at the empty member table:
>>> from members.models import Members
>>> Members.objects.all()
# Outputs >QuerySet [ ]>

A QuerySet is a collection of data from a database.
Add a record to the table, by executing these two lines:
>>>member = Members(firstname = 'Yateesh', lastname = 'Chandra')
>>>member.save()
>>>Members.objects.all().values()

How to add Multiple Records:
>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save()

>>> Members.objects.all().values() 	# It is just like SELECT statement from SQL


Update Data:
- Lets us assign the record we want to modify to a variable.
>>> x = Members.objects().all()[4]
>>> x.firstname
# displays the first_name 
>>> x.firstname = "Likith"
>>> x.save()
>>> Member.objects.all().values()


Delete Data:
- It can be done in two ways. We can directly run the query like this :
>>> Members.objects.all()[3].delete()		# Removes the item at index 3

Or else assign to a variable 
>>> x = Members.objects.all()[3]
>>> x.delete()


Update Model:
Go to the  Members class in Model.py and change accordingly:
from django.db import models
from django.utils import timezone

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null = True)
    entry_Date = models.DateField(default = timezone.now, null = True)

#Now Make Migrations :
py manage.py makemigrations members

#Now Migrate
py manage.py migrate

# Add the data to check
>>> mem = Members(firstname = 'Bhaskar', lastname = 'Praveen', phone = '9395660921')
>>> mem.save()


-------------------------------END OF MODULE 1 ---------------------------------------------

-------------------------------MODULE - 2. DISPLAY -------------------------------------- 

Create Template : 
After creating Models, with the fields and data we want in them, it is time to display the data in a web page. Create a HTML file named 'all_members.html' and place in templates folder.

# all_members.html :
<!DOCTYPE html>
<html>
<body>

<h1>Members</h1>
  
<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }} {{ x.lastname }}</li>
  {% endfor %}
</ul>

</body>
</html>

- Do you see the {% %} brackets inside the HTML document?
- They are Django Tags, telling Django to perform some programming logic inside these brackets.

Modify the existing View : 
We can send it to the template like this :

# views.py :
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

The members view does the following :
- Creates a mymember object with all the values of the Member model.
- Loads the all_members.html template
- Creates an object containing the mymembers object.
- Sends the object to the template.
- Outputs the HTML that is rendered by the template.

- (practice-world) C:\Users\Yateesh Chandra\Django-Practice\first_project>py manage.py runserver
Run the above command and check at http://127.0.0.1:8000/members/

Create a new template details.html :
<!DOCTYPE html>
<html>
    <body>
        <h1>{{mymember.firstname}} {{mymember.lastname}}</h1>
        
        <p>
            Phone: {{mymember.phone}}
        </p>
        <p>
            Member since {{mymember.joined_date}}
        </p>
        <p>
            Back To <a href= "/members"> Members</a>
        </p>
    </body>
</html>

Change a little bit code for the all_templates
<!DOCTYPE html>
<html>
    <body>
        <h1>
            Members
        </h1>

        <ul>
            {% for x in mymembers %}
            <li>
                <a href = "details/{{x.id}}">{{x.firstname}} {{x.lastname}}</a>
            </li>
            {% endfor %}
        </ul>
    </body>
</html>

Add the function details() view  from 
# views.py :

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

We need to make sure that the 'details/' url point to the correct view, with id as parameter.

Open the urls.py file and add the details view to the urlspattern list.

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name = "members"),
    path('members/details/<int:id>', views.details, name = 'details'),
]

Then, We have to click on the Name to get the details about that ID from link :
http://127.0.0.1:8000/members/


# Add Master Template

By using The Extend Tag, Django provides a way of making a "parent template" that you can include in all pages to do the stuff that is the same in all pages. Let us start by creating a template called "master.html"

## Master.html :

Now the two templates (all_members.html and details.html) can use this master.html template.

This is done by including the master template with the {% extends %} tag, and inserting a title block and a content black

Modify the all_templates.html a bit :

{% extends "master.html" %}

{% block title %}
    Students - List
{% endblock %}

{% block content}
        <h1>
            Members
        </h1>

        <ul>
            {% for x in mymembers %}
            <li>
                <a href = "details/{{x.id}}">{{x.firstname}} {{x.lastname}}</a>
            </li>
            {% endfor %}
        </ul>
{% endblock %}