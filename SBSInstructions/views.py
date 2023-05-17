import base64, json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from SBSInstructions.form import AnleitungForm
from SBSInstructions.models import Profil, Anleitung, Anleitungsschritt, Komponente

# Create your views here.


class AnleitungerstellenDetailView(DetailView):

    model = Anleitung
    template_name = 'Anleitungerstellen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnleitungForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = AnleitungForm(request.POST, request.FILES)
        if form.is_valid():
            # Zugriff auf die Felder des Anleitung-Modells
            
            profil = Profil.objects.get(user=request.user)  # Hier Profil-Objekt passend zum eingeloggten Benutzer abrufen
            anleittitel = request.POST.get('anleittitel')
            ersteller = request.POST.get('ersteller')
            kategorie = request.POST.get('kategorie')
            dauer = request.POST.get('dauer')
            datum = request.POST.get('datum')
            # Weitere Felder hier auflisten

            # Speichern der Daten in der Datenbank
            anleitung = Anleitung(
                profil=profil,
                anleittitel=anleittitel,
                ersteller=ersteller,
                kategorie=kategorie,
                dauer=dauer,
                datum=datum
            )
            anleitung.save()

            # Speichern des Formulars
            form.save()

            
            return redirect('anleitungerstellenDetailView', pk=self.kwargs['pk'])
        
        else:

            context = self.get_context_data(form=form)
            # Fehlermeldungen für spezifische Felder
            context['titel_error'] = form.errors.get('anleittitel', '')
            context['profil_error'] = form.errors.get('profil', '')
            context['kategorie_error'] = form.errors.get('kategorie', '')
            context['dauer_error'] = form.errors.get('dauer', '')
            return self.render_to_response(context)


class AnleitungdurchgehenDetailView(DetailView):

    model = Anleitung
    template_name = 'Anleitungdurchgehen.html'

    context_object_name = 'anleitung'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anleitung = self.get_object()

        anleitungstitel = Anleitung.anleittitel

        # Listen für Schritte und Komponenten erstellen
        schritt_benennung_list = []
        schritt_benennung_tuple = ()
        komponenten_list = []

        # Schleife durch alle Schritte der Anleitung
        for schritt in anleitung.anleitungsschritt_set.all():
            # Schrittinformationen in die entsprechenden Listen hinzufügen
            schritt_dict = {
                'schrittbennenung': Anleitungsschritt.schrittbenennung,
                'beschreibung': Anleitungsschritt.beschreibung,
                'schrittbild': self.get_base64_image_schritt(Anleitungsschritt.schrittbild)  # Bild in Base64-codierter Form speichern
            }

            # Komponenteninformationen für den aktuellen Schritt in ein Wörterbuch hinzufügen
            komponenten_dict = {}
            for komponente in schritt.komponente_set.all():
                komponenten_dict[komponente.pk] = {
                    'kompbeschreibung': komponente.kompbeschreibung,
                    'kompbild': self.get_base64_image_komponente(komponente.kompbild)  # Bild in Base64-codierter Form speichern
                }

            schritt_dict['komponenten'] = komponenten_dict
            komponenten_list.append(komponenten_dict)

            # Schrittinformationen in die entsprechenden Listen hinzufügen
            schritt_benennung_list.append(schritt_dict)
        
        # Kontextdaten setzen
        context['anleitungstitel'] = anleitungstitel
        # context['schritt_dict'] = json.dumps(schritt_dict)
        context = { 'einzelschritte': list(Anleitungsschritt.objects.values()), 'schritt_dict': tuple(schritt_dict)}

        return context

    # Holt Schrittbild
    def get_base64_image_schritt(self, image):
        """
        Konvertiert ein Bild in Base64-codierter Form.
        """

        with open('media/images/Schrittbilder/pexels-phil-desforges-15185102.jpg', 'rb') as f:
            image_data = f.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
        return image_base64

    # Holt Komponentenbild
    def get_base64_image_komponente(self, image):
        """
        Konvertiert ein Bild in Base64-codierter Form.
        """

        with open('media/images/Komponentenbilder/pexels-phil-desforges-15185102.jpg', 'rb') as f:
            image_data = f.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
        return image_base64


    # def get_base64_image_thumbnail(self, image):
    #     """
    #     Konvertiert ein Bild in Base64-codierter Form.
    #     """

    #     with open(, 'rb') as f:
    #         image_data = f.read()
    #         image_base64 = base64.b64encode(image_data).decode('utf-8')
    #     return image_base64
    
def index(request):
    return render(request, 'Anleitungdurchgehen.html')