from django.db import models

# Create your models here.
class dairy_dataset(models.Model):
    location = models.CharField(max_length=255)
    tot_land_area = models.FloatField()
    num_cows = models.IntegerField()
    price = models.FloatField()
    recording_date = models.DateField()
    farm_size = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    quantity = models.IntegerField()