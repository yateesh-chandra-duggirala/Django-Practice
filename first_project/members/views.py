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
