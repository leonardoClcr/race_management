from django import forms
from corredores.models import Corredores


class CorredorModelForm(forms.ModelForm):
    class Meta:
        model = Corredores
        fields = '__all__'