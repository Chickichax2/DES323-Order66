from django.db import models

# Create your models here.
class dairy_dataset(models.Model):
    location = models.CharField(max_length=255)
    tot_land_area = models.FloatField(default=0)
    num_cows = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    recording_date = models.DateField()
    farm_size = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    added_date = models.DateTimeField(default=timezone.now)