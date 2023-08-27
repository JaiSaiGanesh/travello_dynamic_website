from django.db import models

class Destination(models.Model):
    name=models.CharField()
    img=models.ImageField(upload_to='pics')
    description=models.CharField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)