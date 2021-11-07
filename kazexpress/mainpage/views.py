from django.shortcuts import render
from django.http import HttpResponse
from django.template.context import RequestContext
def index(reqest):
#    context_instance=RequestContext(request)
    return render(reqest,"main.html")
    
# Create your views here.
