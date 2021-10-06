from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)


class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, default='pending')
