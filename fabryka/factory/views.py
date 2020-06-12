from django.http import HttpResponse
from django.template import loader
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Praca, ListaPrac, Opiekun


class HomePageView(TemplateView):
    template_name = 'index.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'


class SearchResultsView(ListView):
    model = ListaPrac
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Praca.objects.filter(
            Q(temat_praca__icontains=query)
        )
        return object_list

    # queryset = Uczen.objects.filter(imie_uczen__icontains='Da')  # new


'''

def search(request):
    query = request.GET.get('q')
    context_dict = None
    if query:
        results = Uczen.objects.filter(imie_uczen=query)
        if results.count():
            context_dict['results'] = results
        else:
            context_dict['no_results'] = query
    return render(request, "test.html", context_dict)


'''


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
