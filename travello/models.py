from django.db import models

# Create your models here.


class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img =  models.ImageField(upload_to='pics')
    desc = models.TextField()
    price =  models.IntegerField()
    offer = models.BooleanField(default=False)
    link = models.TextField()
class News(models.Model):
    date = models.TextField()
    title = models.CharField(max_length=100)
    img =  models.ImageField(upload_to='news')
    category = models.TextField()
    desc = models.TextField()
class Review(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()



