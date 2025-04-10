from django.db import models

# Create your models here.
class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    name_scientific = models.CharField(max_length=50)
    name_common = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    status = models.CharField(max_length=50)
    species_group = models.CharField(max_length=50)
    species_subgroup = models.CharField(max_length=50)

    def __str__(self):
        return self.name_common