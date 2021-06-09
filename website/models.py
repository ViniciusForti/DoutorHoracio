from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Contato(models.Model):
    email = models.EmailField(default=" ")
    texto = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.email)