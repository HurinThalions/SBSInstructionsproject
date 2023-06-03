from dataclasses import field
import datetime
from django import views
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic.edit import FormView
from SBSInstructions import form

from SBSInstructions.form import SignupForm, EmailAuthenticationForm, AnleitungForm, AnleitungsschrittForm, KomponenteForm, SchrittundKomponentenMultiForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente


# Create your views here.

# Startseite
def index(request):

    return render(request, 'Startseite.html')


# Anleitung wurde durchgegangen
def anleitungfertig(request):
    return render(request, 'Anleitungfertig.html')

# Anleitung wurde teilweise erstellt
def entwurffertig(request):
    return render(request, 'Entwurfgespeichert.html')

# Anleitung wurde erstellt
def anleitunggespeichert(request):
    return render(request, 'Anleitunggespeichert.html')


# erste Seite von Anleitungen wird hiermit erstellt
class AnleitungerstellenCreateView(CreateView):

    # Formular um die Daten aufzunehmen und Abzuspeichern
    # siehe form.py
    form_class = AnleitungForm

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungerstellen.html'

    success_url = 'anleitungsschritteerstellen'

    # Falls der Benutzer eingelogt ist soll der Ersteller automatisch ausgefuellt werden
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # ersteller = None

        # if self.request.user.is_authenticated:
        #     ersteller = self.request.user.profil.ersteller

        # kwargs['ersteller'] = ersteller
        kwargs['initial'] = {'datum': datetime.date.today()}
        return kwargs

    
    # Daten werden im Formular gespeichert und zur datenbank geschickt
    def form_valid(self, form):
        
        form.instance.datum = datetime.date.today()
        return super().form_valid(form)

class AnleitungsschritterstellenCreateView(CreateView):

    template_name = 'Anleitungsschritterstellen.html'

    form_class = AnleitungsschrittForm

    success_url = 'komponentenerstellen'

    def form_valid(self, form):
        anleitung = Anleitung.objects.latest('id')
        form.save_with_anleitung_id(anleitung)
        return super().form_valid(form)

class KomponentenerstellenCreateView(CreateView):
    template_name = 'Komponentenerstellen.html'
    form_class = KomponenteForm
    success_url = 'anleitungsschritteerstellen'

    def form_valid(self, form):
        anleitungsschritt = Anleitungsschritt.objects.latest('id')
        form.save_with_anleitungsschritt_id(anleitungsschritt)
        return super().form_valid(form)



# Anleitungen koennen hier durchgegangen werden
class AnleitungdurchgehenDetailView(DetailView):

    #  Definierung des Models das verwendet wird
    model = Anleitung

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungdurchgehen.html'
    
    # Holen der Daten aus der Datenbank und werden in den Kontext, der zur HTML und Javascript geschickt wird, gepackt
    def get_context_data(self, **kwargs):

        # Holt die Anleitung
        context = super().get_context_data(**kwargs)
        anleitung = self.get_object()

        # Kontextdaten setzen
        context = { 'anleitungstitel': anleitung,
                    'einzelschritte': list(Anleitungsschritt.objects.values('id','schrittbenennung', 'beschreibung', 'schrittbild')),
                    'komponenten': list(Komponente.objects.values())}

        return context



# Erstellung des Profils
class ProfilerstellenCreateView(CreateView):

    form_class = SignupForm 
    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profilerstellen.html'

    success_url = 'login'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# Einloggen
class ProfileinloggenLoginView(LoginView):
    template_name = 'Profileinloggen.html'
    authentication_form = EmailAuthenticationForm
    success_url = '/profileigeneanleitungen'
    
# Eigeloggt und nur die selbst erstellten Entwuerfe und Anleitungen werden angezeigt
class ProfileigeneAnleitungenDetailView(DetailView):

    model = Profil
    template_name = 'Profileigeneanleitungen.html'




# Anleitungsschritt und Komponenten werden in einem Schritt aufgenommen. Funktioniert noch nicht
# Anleitungsschritte werden erstellt
# class AnleitungsschritterstellenCreateView(FormView):

#     form_class = SchrittundKomponentenMultiForm

#     template_name = 'Anleitungsschritterstellen.html'


