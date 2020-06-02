from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def logowanie(request):
    template = loader.get_template('Logowanie.html')
    return HttpResponse(template.render())
