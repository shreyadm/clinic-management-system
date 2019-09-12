from django.db import models

# Create your models here.

class Login(models.Model):
    user = models.CharField(max_length=25)
    pas = models.CharField(max_length=25)