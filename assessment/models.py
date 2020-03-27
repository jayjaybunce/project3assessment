from django.db import models

# Create your models here.
class WishItem(models.Model):
    content = models.CharField(max_length=200)