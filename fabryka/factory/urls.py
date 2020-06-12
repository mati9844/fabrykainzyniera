from django.conf.urls import url
from django.urls import path

from . import views

#
from django.views.generic.base import TemplateView
#

urlpatterns = [
    #path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('',  views.HomePageView.as_view(), name='index'),
    path('user/', views.user_page, name='home'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
