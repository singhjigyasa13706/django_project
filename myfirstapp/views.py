from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to my First Django app!</h1>")

# Create your views here.
