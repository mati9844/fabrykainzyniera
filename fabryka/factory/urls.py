from django.conf.urls import url
from django.urls import path

from . import views

#
from django.views.generic.base import TemplateView
#

urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.logowanie, name='Logowanie'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('user/', TemplateView.as_view(template_name='Strona-2.html'), name='home'),

]
