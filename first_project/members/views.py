from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
