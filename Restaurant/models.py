from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Booking(models.Model):
    ID = models.IntegerField(validators=[MaxValueValidator(11)])
    Name = models.CharField(max_length = 255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(20)])
    BookingDate = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    ID = models.IntegerField(validators=[MaxValueValidator(5)])
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(11)])
