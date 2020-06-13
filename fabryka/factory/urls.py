from django.conf.urls import url
from django.urls import path

from . import views

#
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
#

urlpatterns = [
    path('',  views.HomePageView.as_view(), name='index'),
    path('user/', login_required(views.ProfileView.as_view()), name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
