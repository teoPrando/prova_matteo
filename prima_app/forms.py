"""
PERCHE SERVE FORMS.PY?
In questo modo django:
-Crea in automatico il form html
-Valida i dati
-Crea gli oggetti python
-Salva nel database
"""
from django import forms
from .models import Meccanico,Autovettura

class MeccanicoForm(forms.ModelForm): # Django legge il modello (model=meccanico) e crea automanticamente il form html
    class Meta: #obbligatoria
        model = Meccanico #specifica la classe dell'oggetto che si vuole inserire definita in models.py deve essere inserita
        fields = ['nome', 'cognome'] # specifica quali campi devono essere chiesti di inserire nel form

class AutovetturaForm(forms.ModelForm): 
    class Meta: #obbligatoria
        model = Autovettura #specifica la classe dell'oggetto che si vuole inserire definita in models.py deve essere inserita
        fields = ['targa', 'marca','modello'] # specifica quali campi devono essere chiesti di inserire nel form
