from django.db import models
from django.urls import reverse
from datetime import date
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.

class Toy(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    nature = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)

        # changing this instance method does not imapact data base, threfore no migration needed
    def __str__(self):
        return f'{self.name} ({self.id})'

    
    def get_absolute_url(self):
      return reverse('detail', kwargs={'pokemon_id': self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
   date = models.DateField('Feeding Date')
   meal = models.CharField(
   max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
   )     

   pokemon = models.ForeignKey(
    Pokemon,
    on_delete=models.CASCADE
  )

   pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
   
   def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
   class Meta:
        ordering = ['-date']
