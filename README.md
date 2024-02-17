#**-------------------------------MODULE - 1. DJANGO -------------------------------------- **#

### Django : 
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
-- Run the server


## Templates:
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
-- Outputs >QuerySet [ ]>

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

## Add the data to check
>>> mem = Members(firstname = 'Bhaskar', lastname = 'Praveen', phone = '9395660921')
>>> mem.save()


#-------------------------------END OF MODULE 1 -------------------------------------------#

#-------------------------------MODULE - 2. DISPLAY --------------------------------------#

Create Template : 
After creating Models, with the fields and data we want in them, it is time to display the data in a web page. Create a HTML file named 'all_members.html' and place in templates folder.

## all_members.html :
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

## views.py :
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
## views.py :

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

We need to make sure that the 'details/' url point to the correct view, with id as parameter.

Open the urls.py file and add the details view to the urlspattern list.

## urls.py
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

# Add Main Index Page

Let us create a main page that lands us when we open the default page "127.0.0.1:8000/"
{% extends "master.html" %}

{% block title %}
    Students
{% endblock %}

{% block content %}
    <h1>
        Students Group
    </h1>

    <h3>
        Students
    </h3>

    <p>
        Check out all our <a href="members/">members</a>
    </p>
{% endblock %}


Add the root URL to the urls.py path :
path('', views.main, name = "main")


- Add 404 Template :
For this, We need to change the settings.py by setting to :
    DEBUG = False
    ALLOWED_HOSTS = ['*']    //Set a proper host when DEBUG is set to false.

By default, The settings.py searches for 404.html in the templates 
Or else We can set a customized 404.html from templates folder of members according to our wish.

# 404.html
<!DOCTYPE html>
<html>
    <body>
        <h1>
            OOPS...!
        </h1>
        <p>
            Unable to load the requested file.
        </p>
    </body>
</html>

Now if any api is applied in the address bar that does not exist, we will get 404 template.

- Add Test View 
We can test code without interrupting the main project.
We can add a test view that is exactly like the one we create :

- Let us add a view called "testing" in the views.py

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits' : ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))

- We have to redirect the testing view to url "/testing" and add it to the urls.py
    path('testing/', views.testing, name = 'testing'),

- Create a Template 'template.html'
<!DOCTYPE html>
<html>
    <body>
        {% for x in fruits %}
            <h1>{{x}}</h1>
        {% endfor %}

        <p>In Views.py you can see what the fruits variable looks like...</p>
    </body>
</html>

Run the server at 127.0.0.1:8000/testing to check how it is working.

#-------------------------------END OF MODULE 2 -------------------------------------------#

#-------------------------------MODULE - 3. DISPLAY --------------------------------------#

# Django Admin :
Django Admin is actually a CRUD user interface of all models.!
To enter the admin user interface, start the server by navigating to the folder and execute this command :
py manage.py runserver -- and check at 127.0.0.1:8000/admin/

This leads to admin because of the file : my_tennis_club/my_tennis_club/urls.py

The urlpatterns[] list takes requests going to admin/ and sends them to admin.site.urls, which is a part of a built-in application that comes with Django and contains a lot of functionality and user interfaces, one of them being the log-in user interface.

- Create User:
To be able to log into the admin application, we need to create a user.
py manage.py createsuperuser

SNAPSHOT :
Username (leave blank to use default name): shiva
Email address: shiva@gmail.com
Password: shiva
Password (again): shiva
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

Just runserver and go to "/admin"
After that DJANGO Administration , It will site administration - Authentication and Authorization. We can Add groups and users here

The members model is missing, as it should be, you have to tell Django which models that should be visible in the admin interface

# Include Member in the Admin Interface
To include, The member model in the admin interface, we have to tell Django that this model should be visible in the admin interface. This is done in a file called admin.py and is located in your app's folder, which in our case in the members folder. Open it and it should look like this:

Insert a couple of lines here to make the member model visible in the admin page in admin.py :

from django.contrib import admin
from .models import Members

admin.site.register(Members)

Now when we see admin page is registered with Models, We get Members operation along with Group and Users

Click 'Members' and see the records that we inserted and when we click on the Member Object, We can see the details

By default, "Member Object (1)" is visible instead of "firstname" and "lastname". 

We can Set the List Display.

# Make the list Display More Reader-Friendly
When you display a model as a list, Django displays each record as the string representation of the record object, which in our case is "Member Object(1)"

To change this to a more reader-friendly format, we have two choices:
1. Change the string representation function, __str__() of the Member Model
2. Set the list_details property of the Member Model

Add this in models.py:
def __str__(self):
    return f"{self.firstname} {self.lastname}"

# Set list_display
- We can control the fields to display by specifying them in a list_display property in the admin.py
- First create a MemberAdmin() class and specify the list_display tuple, like this.

Change in the admin.py :

from django.contrib import admin
from .models import Members

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname", "entry_Date")

admin.site.register(Members, MemberAdmin)

# Update Members
- Now we are able to create, update and delete members in our database and we start by giving them all a date when they become members

Click the first member, Bhaskar to open the record for editing, and give him a joined_date.

# Add Members 
- We can add members into our Database and fill valid details

# Delete Members
- We can delete Members from the list as well from the http://127.0.0.1:8000/admin/members/members/ .