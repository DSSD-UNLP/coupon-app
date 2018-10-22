from django.db import models
from django.core.validators import MinValueValidator

class Coupon(models.Model):
	name         = models.CharField(max_length = 100, unique = True)
	availability = models.PositiveIntegerField(validators = [MinValueValidator(1)], default = 1)
	percentage   = models.FloatField()
