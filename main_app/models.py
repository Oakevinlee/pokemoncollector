from django.db import models
from django.urls import reverse

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    nature = models.CharField(max_length=100)

# changing this instance method does not imapact data base, threfore no migration needed

    def __str__(self):
        return f'{self.name} ({self.id})'

    
    def get_absolute_url(self):
      return reverse('detail', kwargs={'pokemon_id': self.id})
