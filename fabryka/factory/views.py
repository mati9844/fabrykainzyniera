from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.generic.base import TemplateView


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


@login_required(login_url='/accounts/login/')
def user_page(request):
    # if not request.user.is_authenticated:
    #    return HttpResponseRedirect('accounts/login/')
    template = loader.get_template('Strona-2.html')
    return HttpResponse(template.render())
    # return HttpResponse(TemplateView.as_view(template_name='Strona-2.html'))


'''


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('accounts/login/')

        # Code to be executed for each request/response after
        # the view is called.

        return response
'''
