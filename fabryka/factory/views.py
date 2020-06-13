from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import ListaPrac
from django.contrib.auth import get_user_model


class HomePageView(TemplateView):
    template_name = 'index.html'


class ProfileView(ListView):
    model = ListaPrac
    template_name = 'profile.html'

    def get_queryset(self):
        query = self.request.user.username
        User = get_user_model()
        object_list = ListaPrac.objects.filter(
            Q(opiekun_praca__username=query))
        return object_list


class SearchResultsView(ListView):
    model = ListaPrac
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        query = query.strip()
        if " " in query:
            txt = query.split()
            object_list = ListaPrac.objects.filter(
                (Q(opiekun_praca__last_name__icontains=txt[0]) &
                 Q(opiekun_praca__first_name__icontains=txt[1])) |
                (Q(opiekun_praca__first_name__icontains=txt[0]) &
                 Q(opiekun_praca__last_name__icontains=txt[1])))
        else:
            object_list = ListaPrac.objects.filter(
                Q(opiekun_praca__last_name__icontains=query) |
                Q(opiekun_praca__first_name__icontains=query))
        return object_list


'''
class ClientUploadDelete(DeleteView):
    model = ListaPrac
    success_url = reverse_lazy('dashboard')
    template_name = 'profile.html'
'''
