from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView

from SBSInstructions.form import ProfileinloggenForm, AnleitungForm, SchrittundKomponentenMultiForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente


# Create your views here.

# Startseite
def index(request):

    return render(request, 'Startseite.html')


# erste Seite von Anleitungen wird hiermit erstellt
class AnleitungerstellenCreateView(CreateView):

    model = Profil

    # Formular um die Daten aufzunehmen und Abzuspeichern
    # siehe form.py
    form_class = AnleitungForm

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungerstellen.html'

    # Falls der Benutzer eingelogt ist soll der Ersteller automatisch ausgefuellt werden
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        ersteller = None

        # if self.request.user.is_authenticated:
        #     ersteller = self.request.user.profil.ersteller

        # kwargs['ersteller'] = ersteller
        return kwargs

    # Daten werden im Formular gespeichert und zur datenbank geschickt
    def form_valid(self, form):
        return super().form_valid(form)

# Anleitungsschritte werden erstellt
class AnleitungsschritterstellenCreateView(CreateView):

    # Formular um die Daten aufzunehmen und Abzuspeichern
    # Multiform um die Komponenten auf der selben Seite und zeitgleich abspeichern zu koennen
    form_class = SchrittundKomponentenMultiForm

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Anleitungsschritterstellen.html'


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

class AnleitungfertigDetailView(DetailView):

    template_name = 'Anleitungfertig.html'


# Erstellung des Profils
class ProfilerstellenCreateView(CreateView):

    # Model Formular um die Daten aufzunehmen und Abzuspeichern 
    model = Profil

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profilerstellen.html'
  

# Einloggen
class ProfileinloggenLoginView(LoginView):
    
    # Definierung des Models, um die eingaben mit den daten in der Datenbank abzugleichen
    model = Profil

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profileinloggen.html'

    authentication_form = ProfileinloggenForm

    success_url = reverse_lazy('profileigeneanleitungen')

# Eigeloggt und nur die selbst erstellten Entwuerfe und Anleitungen werden angezeigt
class ProfileigeneAnleitungenDetailView(DetailView):

    model = Profil
    template_name = 'Profileigeneanleitungen.html'

