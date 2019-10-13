from django.db import models

# Create your models here.
class destinations(models.Model):
    name= models.CharField(max_length=200)
    image= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.FloatField()
    offer= models.BooleanField(default=False)

    