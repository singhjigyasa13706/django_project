from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from index!")

def blog_index(request):
    return HttpResponse("Hello from home!")