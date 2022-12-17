# A Django model represents a single entity from the ERD
# The Model is used to perform CRUD database operations

# When we retrieve data from the database using a Model we have model objects
# Each model object (aka instances of the Model) represents a row in a database table

from django.db import models
from django.urls import reverse
from datetime import date, time
from django.contrib.auth.models import User

TYPES = (
    ('TropF','Tropical Freshwater'),
    ('TempF','Temperate Freshwater'),
    ('TropM','Tropical Marine'),
    ('TempM','Temparate Marine'),
    ('Ter','Terrarium'),
    ('E','Enclosure'),
    ('O','Other'),
)

class Enclosure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    type = models.CharField(
        max_length=5,
        choices=TYPES,
        default=TYPES[6][0],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # returns string representation of the model object
    def __str__(self):
        return self.name

    # reverse will return the correct path for the detail named route by attaching id
    def get_absolute_url(self):
        return reverse('detail', kwargs={'enclosure_id': self.id})


class Animal(models.Model):
    given_name = models.CharField(max_length=250)
    common_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    quantity = models.IntegerField()

    # Create foreign key for Enclosure
    # on_delete: when an enclosure is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    parameter = models.CharField(max_length=250)
    units = models.CharField(max_length=50)
    ideal_range = models.CharField(max_length=250)
    frequency = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)

    # Create foreign key for Enclosure
    # on_delete: when an enclosure is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def __str__(self):
        return self.parameter


class ParameterLog(models.Model):
    date = models.DateField()
    time = models.TimeField(blank = True)
    value = models.CharField(max_length=250)

    # Create foreign key for Enclosure and Parameter
    # on_delete: when an enclosure or parameter is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ['-date']