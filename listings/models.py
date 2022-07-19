from django.db import models
from realtors.models import Realtors

date = "photos/%Y/%m/%d"


# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=30)
    state = models.CharField(max_length=200)
    price = models.FloatField()
    has_garden = models.BooleanField()
    has_garage = models.BooleanField()
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    rooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to=date)
    for i in range(1, 7):
        locals()[f'photo{i}'] = models.ImageField(upload_to=date, blank=True)
    list_date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
