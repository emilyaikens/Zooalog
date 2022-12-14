# A Django model represents a single entity from the ERD
# The Model is used to perform CRUD database operations

# When we retrieve data from the database using a Model we have model objects
# Each model object (aka instances of the Model) represents a row in a database table

from django.db import models
from django.urls import reverse
from datetime import date, time
from django.contrib.auth.models import User

TYPES = (
    ('TROPF','Tropical Freshwater'),
    ('TEMPF','Temperate Freshwater'),
    ('TROPM','Tropical Marine'),
    ('TEMPM','Temparate Marine'),
    ('TER','Terrarium'),
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
    ideal_range = models.CharField(max_length=250, blank=True)
    frequency = models.CharField(max_length=250, blank=True)
    notes = models.CharField(max_length=250, blank=True)

    # Create foreign key for Enclosure
    # on_delete: when an enclosure is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def __str__(self):
        return self.parameter


class ParameterLog(models.Model):
    # Create foreign key for Parameter
    # on_delete: when parameter is deleted, all of its children will also be deleted
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)
    date = models.DateField()
    time = models.CharField(max_length=200)

    class Meta:
        ordering = ['-date']


class Diet(models.Model):
    diet_type = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    frequency = models.CharField(max_length=250, blank=True)
    notes = models.CharField(max_length=250, blank=True)

    # Create foreign key for Enclosure
    # on_delete: when an enclosure is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def __str__(self):
        return self.diet_type


class DietLog(models.Model):
    # Create foreign key for Diet
    # on_delete: when diet is deleted, all of its children will also be deleted
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=200)
    notes = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['-date']