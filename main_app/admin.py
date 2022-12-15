from django.contrib import admin
from .models import Enclosure, Animal, Parameter

# Models registered here
admin.site.register(Enclosure)
admin.site.register(Animal)
admin.site.register(Parameter)
