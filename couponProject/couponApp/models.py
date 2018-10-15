from django.db import models

# Create your models here.

class Coupon(models.Model):
	name         = models.CharField(max_length=100, unique=True)
	availability = models.IntegerField(default=1)
	percentage   = models.FloatField()