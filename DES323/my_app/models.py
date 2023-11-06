from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class dairy_dataset(models.Model):
    location = models.CharField(max_length=255)
    tot_land_area = models.FloatField()
    num_cows = models.IntegerField()
    price = models.FloatField()
    recording_date = models.DateField()
    farm_size = models.CharField(max_length=255, default=None)
    product_type = models.CharField(max_length=255, default=None)
    quantity = models.IntegerField(default=0)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    added_date = models.DateTimeField(default=timezone.now)

class user(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    passworld = models.CharField(max_length=100)
