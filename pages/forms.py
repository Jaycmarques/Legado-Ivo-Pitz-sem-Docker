from django import forms
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
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite sua dedicatória'}),
        }
