
from django.http import HttpResponse

# Create your views here.

def index(  request):
    return HttpResponse("Hello this is the index page of the app.")

def details(req):
    return HttpResponse("this is the details")