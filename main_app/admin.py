from django.contrib import admin
from .models import Enclosure, Animal, Parameter, ParameterLog, Diet

# Models registered here
admin.site.register(Enclosure)
admin.site.register(Animal)
admin.site.register(Parameter)
admin.site.register(ParameterLog)
admin.site.register(Diet)
