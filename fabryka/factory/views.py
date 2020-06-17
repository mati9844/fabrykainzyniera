from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import ListaPrac, Praca, Uczen, Wydzial
from django.contrib.auth import get_user_model

from django.shortcuts import render
from datetime import date, datetime
from django.views.generic.edit import FormMixin


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

    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST.get('temat_praca'):
                listaPrac = ListaPrac()
                praca = Praca()
                praca.temat_praca = request.POST.get('temat_praca')
                praca.save()
                listaPrac.temat_praca = praca
                listaPrac.opiekun_praca = request.user
                listaPrac.save()
            if request.POST.get('del_btn'):
                try:
                    pointed_topic = ListaPrac.objects.get(
                        pk=request.POST.get('del_btn'))
                    # check if user is owner of topic
                    if pointed_topic.opiekun_praca == self.request.user:
                        pointed_topic.temat_praca.delete()
                except:
                    pass

            if request.POST.get('change_btn'):
                pointed_topic = ListaPrac.objects.get(
                    pk=request.POST.get('change_btn'))
                if pointed_topic.opiekun_praca == self.request.user:
                    uczen = Uczen()
                    uczen.imie_uczen = request.POST.get('student_first_name')
                    uczen.nazwisko_uczen = request.POST.get(
                        'student_last_name')
                    uczen.indeks_uczen = request.POST.get('student_index')
                    uczen.wydzial_uczen = Wydzial.objects.first()
                    uczen.save()
                    pointed_topic.uczen_praca = uczen
                    pointed_topic.termin_praca = datetime.now()
                    pointed_topic.save()
                    # print(request.POST.get('change_btn'))
                    # print(request.POST.get('student_first_name'))
                    # print(request.POST.get('student_last_name'))
                    # print(request.POST.get('student_index'))
        return super(ProfileView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


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
