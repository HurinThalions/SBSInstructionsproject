from django import forms

from .models import Anleitung, Anleitungsschritt, Komponente

class AnleitungForm(forms.ModelForm):
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
        fields = ('anleitungsschritt', 'kompbild')

