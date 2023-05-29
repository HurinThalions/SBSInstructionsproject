import base64
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView

from SBSInstructions.form import AnleitungForm, AnleitungsschrittForm, KomponenteForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente

# Create your views here.

def index(request):

    return render(request, 'Startseite.html')

class AnleitungerstellenCreateView(CreateView):

    model = Anleitung
    form_class = AnleitungForm

    template_name = 'Anleitungerstellen.html'
    success_url = 'anleitungsschritteerstellen'

class AnleitungsschritterstellenCreateView(CreateView):

    template_name = 'Anleitungsschritterstellen.html'
    form_class = AnleitungsschrittForm
    success_url = '/anleitungdurchgehen/1'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['komponente_form'] = KomponenteForm(self.request.POST)
        else:
            context['komponente_form'] = KomponenteForm()
        return context

    
    def form_valid(self, form):
        context = self.get_context_data()
        komponente_form = context['komponente_form']

        return super().form_valid(form)
        if komponente_form.is_valid():
            self.object = form.save()
            Komponente = komponente_form.save(commit=False)
            Komponente.anleitungsschritt_id = self.object.id
            Komponente.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AnleitungdurchgehenDetailView(DetailView):

    model = Anleitung
    template_name = 'Anleitungdurchgehen.html'

    context_object_name = 'anleitung'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # anleitung = self.get_object()

        # Kontextdaten setzen
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
