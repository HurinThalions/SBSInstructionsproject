from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from betterforms.multiform import MultiModelForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Anleitung, Anleitungsschritt, Komponente

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
