# import base64
from datetime import datetime
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, CreateView

from SBSInstructions.form import ProfilForm, AnleitungForm, SchrittundKomponentenMultiForm
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
    form_class = ProfilForm

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profilerstellen.html'
  

# Einloggen
class ProfileinloggenDetailView(DetailView):
    
    # Definierung des Models, um die eingaben mit den daten in der Datenbank abzugleichen
    model = Profil

    # Template die verwendet wird, um die Seite zu rendern
    template_name = 'Profileinloggen.html'


# Eigeloggt und nur die selbst erstellten Entwuerfe und Anleitungen werden angezeigt
class ProfileigeneAnleitungenDetailView(DetailView):

    model = Profil
    template_name = 'Profil'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profil = self.get_object()

        context = { ''}

    # Holt Schrittbild
    # def get_base64_image_schritt(self, image):
    #     """
    #     Konvertiert ein Bild in Base64-codierter Form.
    #     """

    #     with open('media/images/Schrittbilder/pexels-phil-desforges-15185102.jpg', 'rb') as f:
    #         image_data = f.read()
    #         image_base64 = base64.b64encode(image_data).decode('utf-8')
    #     return image_base64

    # # Holt Komponentenbild
    # def get_base64_image_komponente(self, image):
    #     """
    #     Konvertiert ein Bild in Base64-codierter Form.
    #     """

    #     with open('media/images/Komponentenbilder/pexels-phil-desforges-15185102.jpg', 'rb') as f:
    #         image_data = f.read()
    #         image_base64 = base64.b64encode(image_data).decode('utf-8')
    #     return image_base64


    # def get_base64_image_thumbnail(self, image):
    #     """
    #     Konvertiert ein Bild in Base64-codierter Form.
    #     """

    #     with open(, 'rb') as f:
    #         image_data = f.read()
    #         image_base64 = base64.b64encode(image_data).decode('utf-8')
    #     return image_base64
