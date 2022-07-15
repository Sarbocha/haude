from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=20, default="0000")
    desc = models.TextField()
    date = models.DateField()
