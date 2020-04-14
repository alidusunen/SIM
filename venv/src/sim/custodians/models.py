from django.db import models

class Custodian(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    #To retun name instead od ID number when refered in other areas
    def __str__(self):
        return self.name


# Create your models here.
