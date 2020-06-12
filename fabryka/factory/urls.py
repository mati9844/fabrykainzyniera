from django.conf.urls import url
from django.urls import path

from . import views

#
from django.views.generic.base import TemplateView
#

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    #path('',  views.index, name='index'),
    path('user/', views.user_page, name='home'),

]
