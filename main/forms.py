from .models import Card
from .models import Player
from django import forms
from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["title", "release", "quantity","foil"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название карты'
            }),
            "release": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название выпуска'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
            }),
            
            "foil": CheckboxInput(attrs={
                'placeholder': 'foil',
            }),
        }

class Code(forms.Form):
    code=forms.CharField(label='Code', max_length="100")
