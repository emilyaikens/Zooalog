from django.forms import ModelForm
from .models import Animal

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['given_name', 'common_name', 'scientific_name', 'quantity']