from django.db import HttpResponse

def home(request):
    return HttpResponse('Hello World!')
