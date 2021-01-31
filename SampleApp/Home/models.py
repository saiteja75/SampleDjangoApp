from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    phno = models.CharField(max_length=12)
    msg = models.TextField(max_length=256)
    datetime = models.DateTimeField()
