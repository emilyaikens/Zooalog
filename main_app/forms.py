from django.forms import ModelForm
from .models import Animal, Parameter

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = [
            'given_name', 
            'common_name', 
            'scientific_name', 
            'quantity'
        ]

class ParameterForm(ModelForm):
    class Meta:
        model = Parameter
        fields = [
            'parameter',
            'units',
            'ideal_range',
            'frequency',
            'notes'
        ]