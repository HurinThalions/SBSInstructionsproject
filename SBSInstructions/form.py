from django import forms
from betterforms.multiform import MultiModelForm
from django.contrib.auth.forms import AuthenticationForm

from .models import Profil, Anleitung, Anleitungsschritt, Komponente

class ProfileinloggenForm(AuthenticationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    class Meta:

        fields = ('email', 'password')

class AnleitungForm(forms.ModelForm):

    def __init__(self, **kwargs):
        ersteller = kwargs.pop('ersteller', None)
        super().__init__(**kwargs)
        self.fields['ersteller'].initial = ersteller
                
    class Meta:
        model = Anleitung
        fields = ('profil', 'anleittitel', 'ersteller', 'kategorie','dauer', 'datum', 'img')

class AnleitungsschrittForm(forms.ModelForm):
    class Meta:
        model = Anleitungsschritt
        fields = ('anleitung', 'schrittbenennung', 'beschreibung', 'schrittbild')

class KomponenteForm(forms.ModelForm):
    class Meta:
        model = Komponente
        fields = ('anleitungsschritt', 'kompbeschreibung', 'kompbild')

class SchrittundKomponentenMultiForm(MultiModelForm):
    form_classes = {
        'Anleitungsschritt': AnleitungsschrittForm,
        'Komponente': KomponenteForm,
    }
