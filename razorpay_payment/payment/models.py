from django.db import models

# Create your models here.

class Razor(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Razor"
        verbose_name_plural = "Razors"