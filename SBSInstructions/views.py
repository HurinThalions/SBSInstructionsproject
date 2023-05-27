import base64, json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from SBSInstructions.form import AnleitungForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente

# Create your views here.

class AnleitungerstellenAddPageCreateView(CreateView):

    model = Anleitung
    form_class = AnleitungForm

    template_name = 'AnleitungerstellenAddPage.html'
    success_url = 'anleitungdurchgehen/1'


class AnleitungdurchgehenDetailView(DetailView):

    model = Anleitung
    template_name = 'Anleitungdurchgehen.html'

    context_object_name = 'anleitung'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # anleitung = self.get_object()

        anleitungstitel = Anleitung.anleittitel
       
        # Kontextdaten setzen
        context['anleitungstitel'] = anleitungstitel
        context = { 'anleitungstitel': Anleitung.objects.get(pk=self.kwargs['pk']).anleittitel,
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
