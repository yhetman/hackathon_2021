from django.db import models


class OurImg(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
