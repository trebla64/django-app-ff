from django.db import models


class Client(models.Model):
    email = models.CharField(max_length=200)

class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)