# A Django model represents a single entity from the ERD
# The Model is used to perform CRUD database operations

# When we retrieve data from the database using a Model we have model objects
# Each model object (aka instances of the Model) represents a row in a database table

from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    number = models.IntegerField()

    # returns string representation of the model object
    def __str__(self):
        return self.name