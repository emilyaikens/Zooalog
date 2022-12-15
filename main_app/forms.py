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

    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        self.fields['given_name'].required = False
        self.fields['scientific_name'].required = False
        self.fields['quantity'].required = False


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
    
    def __init__(self, *args, **kwargs):
        super(ParameterForm, self).__init__(*args, **kwargs)
        self.fields['ideal_range'].required = False
        self.fields['frequency'].required = False
        self.fields['notes'].required = False