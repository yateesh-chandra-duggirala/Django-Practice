from django.template import loader
from .models import Members
from django.http import HttpResponse

# Define the view function named 'members' that handles requests related to a members.
def members(request):

    # Retrieve all Member objects from the database and get their values as a Queryset.
    mymembers = Members.objects.all().values()

    # Loads the "all_members.html" template
    template = loader.get_template('all_members.html')
    
    # Prepare the context data to be passed to the template
    context = {
        'mymembers' : mymembers
    }

    # Render the template with the provided context and return it as an HTTP Response.
    # Sends the object to the template
    # Outputs the HTML that is rendered by the template.
    return HttpResponse(template.render(context, request))

# Define the value function named 'details' that handles requests for member details
def details(request, id) :

    # Retrieve a specific member object from the database based on the the provided id
    mymember = Members.objects.get(id = id)
    
    # Load the "details" template.
    template = loader.get_template('details.html')

    # Prepare the contexr data to be passed to the template.
    context = {
        'mymember' : mymember
    }

    # Render the template with the provided context and return it as an HTTP response
    return HttpResponse(template.render(context, request))
