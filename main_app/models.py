# A Django model represents a single entity from the ERD
# The Model is used to perform CRUD database operations

# When we retrieve data from the database using a Model we have model objects
# Each model object (aka instances of the Model) represents a row in a database table

from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TYPES = (
    'Tropical Freshwater',
    'Temperate Freshwater',
    'Tropical Marine',
    'Temparate Marine',
    'Terrarium',
    'Enclosure',
    'Other',
)

class Enclosure(models.Model):
    name = models.CharField(max_length=100,)
    description = models.TextField(max_length=250)
    type = models.CharField(
        max_length=1,
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
    num_ind = models.IntegerField()

    # Create foreign key for Enclosure
    # on_delete: when an enclosure is deleted, all of its children will also be deleted
    enclosure = models.ForeignKey(Enclosure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    # class Meta:
    #     ordering = ['-date']