from django.db import models

# Create your models here.

class SaveData(models.Model):
    picture = models.ImageField(upload_to='./photo/', null=True, blank=True)

