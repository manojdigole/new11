from django.db import models

# Create your models here.


class Contactdata(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    name = models.CharField(max_length=50 ,default=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

