from django.forms import ModelForm
from .models import Sub

class SubForm(ModelForm):
    class Meta:
        model = Sub
        fields = ['date', 'description']