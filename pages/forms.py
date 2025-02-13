from django import forms
from django_summernote.widgets import SummernoteWidget
from pages.models import Dedicatoria

class DedicatoriaForm(forms.ModelForm):
    class Meta:
        model = Dedicatoria
        fields = ['name', 'message']
        labels = {
            'name': 'Seu Nome',
            'message': 'Sua Dedicatória',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'message': SummernoteWidget(attrs={'class': 'form-control', 'placeholder': 'Digite sua dedicatória'}),
        }
