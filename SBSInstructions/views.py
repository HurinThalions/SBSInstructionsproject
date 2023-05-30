# import base64
from datetime import datetime
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, CreateView

from SBSInstructions.form import AnleitungForm, SchrittundKomponentenMultiForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente


# Create your views here.

def index(request):

    return render(request, 'Startseite.html')

class AnleitungerstellenCreateView(CreateView):
    model = Profil
    form_class = AnleitungForm
    template_name = 'Anleitungerstellen.html'
    success_url = 'anleitungdurchgehen/1'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        ersteller = None

        # if self.request.user.is_authenticated:
        #     ersteller = self.request.user.profil.ersteller

        # kwargs['ersteller'] = ersteller
        kwargs['initial'] = {'datum': datetime.today()}  # Füge das heutige Datum als Initialwert hinzu
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

class AnleitungsschritterstellenCreateView(CreateView):

    template_name = 'Anleitungsschritterstellen.html'
 
    form_class = SchrittundKomponentenMultiForm

    success_url = 'anleitungdurchgehen/1'


class AnleitungdurchgehenDetailView(DetailView):

    model = Anleitung
    template_name = 'Anleitungdurchgehen.html'

    context_object_name = 'anleitung'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anleitung = self.get_object()

        # Kontextdaten setzen
        context = { 'anleitungstitel': anleitung,
                    'einzelschritte': list(Anleitungsschritt.objects.values('id','schrittbenennung', 'beschreibung', 'schrittbild')),
                    'komponenten': list(Komponente.objects.values())}

        return context

class AnleitungfertigDetailView(DetailView):

    template_name = 'Anleitungfertig.html'

    

    # # Holt Schrittbild
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
